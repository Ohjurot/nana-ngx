/*
 *	A CheckBox Implementation
 *	Nana C++ Library(http://www.nanapro.org)
 *	Copyright(C) 2003-2021 Jinhao(cnjinhao@hotmail.com)
 *
 *	Distributed under the Boost Software License, Version 1.0.
 *	(See accompanying file LICENSE_1_0.txt or copy at
 *	http://www.boost.org/LICENSE_1_0.txt)
 *
 *	@file: nana/gui/widgets/checkbox.cpp
 */

#include <nana/gui/widgets/checkbox.hpp>
#include <nana/paint/text_renderer.hpp>
#include <nana/gui/element.hpp>
#include <algorithm>

namespace nana
{
	namespace drawerbase::checkbox
	{
		typedef element::crook_interface::state crook_state;

		struct drawer::implement
		{
			widget * widget_ptr{ nullptr };
			scheme * scheme_ptr{ nullptr };
			bool react{ true };
			bool radio{ false };
			facade<element::crook> crook;
		};

		//class drawer
		drawer::drawer()
			:	impl_(new implement)
		{
		}

		drawer::~drawer()
		{
			delete impl_;
		}

		void drawer::attached(widget_reference widget, graph_reference)
		{
			impl_->widget_ptr = &widget;
			impl_->scheme_ptr =static_cast<scheme*>(api::dev::get_scheme(widget));
			api::dev::enable_space_click(widget, true);
		}

		void drawer::refresh(graph_reference graph)
		{
			auto wdg = impl_->widget_ptr;

			//draw background
			if (!api::dev::copy_transparent_background(*wdg, graph))
				graph.rectangle(true, wdg->bgcolor());

			//draw title
			if (graph.width() > 16 + interval)
			{
				auto title = to_wstring(wdg->caption_native());
				std::wstring_view title_sv{ title.data(), title.size() };

				unsigned pixels = graph.width() - (16 + interval);

				nana::paint::text_renderer tr(graph);
				if (!wdg->enabled())
				{
					graph.palette(true, colors::white);
					tr.render({ 17 + interval, 2 }, title_sv, pixels, paint::text_renderer::mode::word_wrap);
					graph.palette(true, static_cast<color_rgb>(0x808080));
				}
				else
					graph.palette(true, wdg->fgcolor());

				tr.render({ 16 + interval, 1 }, title_sv, pixels, paint::text_renderer::mode::word_wrap);
			}

			//draw crook
			unsigned txt_px = 0, descent = 0, ileading = 0;
			graph.text_metrics(txt_px, descent, ileading);
			txt_px += (descent + ileading);

			auto e_state = api::element_state(*wdg);
			if(!wdg->enabled())
				e_state = element_state::disabled;

			impl_->crook.draw(graph,
				impl_->scheme_ptr->square_bgcolor.get(wdg->bgcolor()), impl_->scheme_ptr->square_border_color.get(wdg->fgcolor()),
				rectangle(0, txt_px > 16 ? (txt_px - 16) / 2 : 0, 16, 16), e_state);
		}

		void drawer::mouse_down(graph_reference graph, const arg_mouse&)
		{
			refresh(graph);
			api::dev::lazy_refresh();
		}

		void drawer::mouse_up(graph_reference graph, const arg_mouse&)
		{
			if (impl_->react)
			{
				impl_->crook.reverse();
				arg_checkbox arg{ static_cast<nana::checkbox*>(impl_->widget_ptr) };
				api::events<nana::checkbox>(impl_->widget_ptr->handle()).checked.emit(arg, impl_->widget_ptr->handle());
			}
			refresh(graph);
			api::dev::lazy_refresh();
		}

		void drawer::mouse_enter(graph_reference graph, const arg_mouse&)
		{
			refresh(graph);
			api::dev::lazy_refresh();
		}

		void drawer::mouse_leave(graph_reference graph, const arg_mouse&)
		{
			refresh(graph);
			api::dev::lazy_refresh();
		}

		drawer::implement * drawer::impl() const
		{
			return impl_;
		}
		//end class drawer
	} //end namespace drawerbase::checkbox

	//class checkbox

		checkbox::checkbox(){}

		checkbox::checkbox(window parent, std::string_view text, bool visible)
		{
			create(parent, rectangle{}, visible);
			caption(text);			
		}

		checkbox::checkbox(window parent, std::wstring_view text, bool visible)
		{
			create(parent, rectangle{}, visible);
			caption(text);			
		}

#ifdef __cpp_char8_t
		checkbox::checkbox(window parent, std::u8string_view text, bool visible)
		{
			create(parent, rectangle{}, visible);
			caption(text);			
		}
#endif

		checkbox::checkbox(window wd, const nana::rectangle& r, bool visible)
		{
            bgcolor(api::bgcolor(wd));
			create(wd, r, visible);
		}

		void checkbox::element_set(const char* name)
		{
			get_drawer_trigger().impl()->crook.switch_to(name);
		}

		void checkbox::react(bool want)
		{
			get_drawer_trigger().impl()->react = want;
		}

		bool checkbox::checked() const
		{
			return (get_drawer_trigger().impl()->crook.checked() != drawerbase::checkbox::crook_state::unchecked);
		}

		void checkbox::check(bool state)
		{
			using crook_state = drawerbase::checkbox::crook_state;
			if (checked() != state)
			{
				get_drawer_trigger().impl()->crook.check(state ? crook_state::checked : crook_state::unchecked);
				api::refresh_window(handle());

				arg_checkbox arg(this);
				this->events().checked.emit(arg, this->handle());
			}
		}

		void checkbox::radio(bool is_radio)
		{
			get_drawer_trigger().impl()->crook.radio(is_radio);
			api::refresh_window(handle());
		}

		void checkbox::transparent(bool enabled)
		{
			if(enabled)
				api::effects_bground(*this, effects::bground_transparent(0), 0.0);
			else
				api::effects_bground_remove(*this);
			api::refresh_window(handle());
		}

		bool checkbox::transparent() const
		{
			return api::is_transparent_background(*this);
		}

		void checkbox::_m_complete_creation()
		{
			bgcolor(api::bgcolor(parent()));
			widget::_m_complete_creation();
		}
	//end class checkbox

	//class radio_group
		radio_group::~radio_group()
		{
			for(auto & e : ui_container_)
			{
				e.uiobj->radio(false);
				e.uiobj->react(true);
				api::umake_event(e.eh_clicked);
				api::umake_event(e.eh_checked);
				api::umake_event(e.eh_destroy);
				api::umake_event(e.eh_keyboard);
			}
		}

		void radio_group::add(checkbox& uiobj)
		{
			uiobj.radio(true);
			uiobj.check(false);
			uiobj.react(false);

			element_tag el;

			el.uiobj = &uiobj;

			el.eh_checked = uiobj.events().checked.connect_unignorable([this](const arg_checkbox& arg)
			{
				if (arg.widget->checked())
				{
					for (auto & ck : ui_container_)
					{
						if (ck.uiobj->handle() != arg.widget->handle())
							ck.uiobj->check(false);
					}
				}
			}, true);

			el.eh_clicked = uiobj.events().click.connect_unignorable([this](const arg_click& arg)
			{
				for (auto & i : ui_container_)
					i.uiobj->check(arg.window_handle == i.uiobj->handle());
			}, true);
			
			el.eh_destroy = uiobj.events().destroy.connect_unignorable([this](const arg_destroy& arg)
			{
				for (auto i = ui_container_.begin(); i != ui_container_.end(); ++i)
				{
					if (arg.window_handle == i->uiobj->handle())
					{
						ui_container_.erase(i);
						return;
					}
				}
			});

			el.eh_keyboard = uiobj.events().key_press.connect_unignorable([this](const arg_keyboard& arg)
			{
				auto window_handle = arg.window_handle;

				auto i = std::find_if(ui_container_.begin(), ui_container_.end(), [window_handle](const element_tag& e){
					return (e.uiobj->handle() == window_handle);
				});
				
				if (ui_container_.end() == i)
					return;

				checkbox * target = nullptr;

				if (keyboard::os_arrow_up == arg.key)
				{
					if (ui_container_.begin() != i)
						target = (i - 1)->uiobj;
					else
						target = ui_container_.back().uiobj;
				}
				else if (keyboard::os_arrow_down == arg.key)
				{
					if (ui_container_.end() - 1 != i)
						target = (i + 1)->uiobj;
					else
						target = ui_container_.front().uiobj;
				}

				if(target)
				{
					target->check(true);
					target->focus();
				}
			});
			
			ui_container_.emplace_back(el);
		}

		std::size_t radio_group::checked() const
		{
			for (auto i = ui_container_.cbegin(); i != ui_container_.cend(); ++i)
			{
				if (i->uiobj->checked())
					return static_cast<std::size_t>(i - ui_container_.cbegin());
			}

			return npos;
		}

		std::size_t radio_group::size() const
		{
			return ui_container_.size();
		}
	//end class radio_group
}//end namespace nana
