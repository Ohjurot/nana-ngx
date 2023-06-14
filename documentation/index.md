---
title: About nana
summary: NGX (Nana Generation X) is a fork of the popular nana C++ GUI library
authors:
    - Ludwig Fuechsl
---

# Nana NGX (**N**ana **G**eneration **X**)
Nana is a cross-platform library (Windows & Linux) for GUI programming in modern C++ style.

## Quick example
This is how fast you can get a result using nana:
```cpp title="Hello Nana"
#include <nana/gui.hpp>
#include <nana/gui/widgets/label.hpp>
#include <nana/gui/widgets/button.hpp>

int main()
{
    using namespace nana;

    //Define a form.
    form fm;

    //Define a label and display a text.
    label lab{fm, "Hello, <bold blue size=16>Nana C++ Library</>"};
    lab.format(true);

    //Define a button and answer the click event.
    button btn{fm, "Quit"};
    btn.events().click([&fm]{
        fm.close();
    });

    //Layout management
    fm.div("vert <><<><weight=80% text><>><><weight=24<><button><>><>");
    fm["text"]<<lab;
    fm["button"] << btn;
    fm.collocate();
	
    //Show the form
    fm.show();

    //Start to event loop process, it blocks until the form is closed.
    exec();
}
```

## Why a fork?
Nana ngx is a fork of the popular C++ GUI library [nana](http://nanapro.org). This fork has 
been created to actively support, promote and evolve nana since the original author has not 
shown any activity for over a year now! (The last nana release was in 2020)

We aim to bring the following improvements to nana:
 
- **Active support and development**: Via GitHub (Open Source)
- **Modern repository layout**: Unified build system, CI and CD (Conan package, Documentation, ...)
- **Better documentation**
- **Extensible**: Allow nana to be more modular and extensible with by users. Provide a common workflow for creating, submitting and publishing extension. TODO: Direct contribution vs. Extension (Solve the problem / define borders)
- **Features**: Improvements and new features 

See our [Roadmap](roadmap-20.md) for a status on nana v2.0
