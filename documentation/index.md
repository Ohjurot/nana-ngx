---
title: About nana
summary: NGX (Nana Generation X) is a fork of the popular nana C++ GUI library
authors:
    - Ludwig Fuechsl
---

# Nana NGX (**N**ana **G**eneration **X**)
Nana is a cross-platform C++ library for GUI programming with a modern C++ style.
!!! warning
    We are currently in the process of developing the last classical nana release (`v1.8-LTS`). Please report the features/fixes that are important for you NOW. Our current platform support is limited to Windows and Linux. This shall change with `v2.x`.

    We will soon begin working on nana NGX (`v2.x`). Feel free to give us your suggestions as well. 

## Quick example
This is how fast you can get a result using nana:
```cpp title="Hello Nana" linenums="1"
#include <nana/gui.hpp>
#include <nana/gui/widgets/label.hpp>
#include <nana/gui/widgets/button.hpp>

int main()
{
    using namespace nana;

    // Define a form.
    form fm;

    // Define a label and display a text.
    label lbl(fm, "Hello, <bold blue size=16>Nana C++ Library</>");
    lbl.format(true);

    // Define a button and answer the click event.
    button btn(fm, "Quit");
    btn.events().click(
        [&fm]()
        {
            fm.close();
        }
    );

    // Layout management
    fm.div("vert <><<><weight=80% text><>><><weight=24<><button><>><>");
    fm["text"] << lbl;
    fm["button"] << btn;
    fm.collocate();
	
    // Show the form
    fm.show();

    // Start to event loop process, it blocks until the form is closed.
    exec();
}
```

## Why a fork?
Nana ngx is a fork of the popular C++ GUI library [nana](http://nanapro.org). This fork has 
been created to actively support, promote and evolve nana since the original author has not 
shown any activity for over a year now! (The last nana release was in 2020)

We aim to bring the following improvements to nana:
 
- **Active support and development**: Via GitHub (Open Source)
- **Features**: Improvements and new features 
- **Modular**: We aim to support as much as possible (ex. png, jpeg). However we will also provide a way to turn off the support and by that the dependencies!
- **Extensible**: Allow nana to be extensible by extensions and the end product. Provide a common workflow for creating, submitting and publishing extension. 
- **Better documentation**: Consistent and consequent documentation in ONE place. Information, API-Reference, Guides, Examples, ... everything shall be hosted in one repo and shall be automatically deployed via GitHub actions to this GitHub page. 
- **Modern repository layout**: Unified CMake and Conan2 based build system. Automation with CI and CD via GitHub actions.  

See our [Roadmap](roadmap-20.md) for a status on nana v2.0
