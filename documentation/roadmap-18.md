---
title: Roadmap to 1.8
summary: We want to bring nana forward. This is our roadmap for version 2.0
authors:
    - Ludwig Fuechsl
---

# Nana 1.8 (Nana LTS)

Nana version 1.8 (LTS - Long Term Support) shall be a drop-in replacement for existing code that uses nana. 

## Progress
- [x] Migration of the old codebase to the new repository
- [ ] Migration and resolve all old Pull-Requests and Issues
- [ ] Revisiting of all control's on a reference Windows and Linux machine. Resolving of breaking bugs
- [ ] Repository Setup for a LTS release

## Support
Currently we provide the following support for exiting applications:

- Drop in replacement when using out SDK or Conan2
- Support via GitHub issues (Tag `v1.8-LTS`)
- Updates to prevent the LTS version from breaking
- Community driven support

We don't support:

- New features
- Documentation
- Commercial support (If you need commercial support contact me at [sales@moxibyte.com](mailto:sales@moxibyte.com))

LTS Support is planed to at least continue until end of 2026. An exact data will be provided as soon as we release v2.0. 

## Open PRs & Issues
If all of the following checkboxes are ticked, then we are ready to publish `v1.8.0` :wink:
### Pull Requests
- [ ] [Removed char8_t support from nana::menu since it was broken and unused.](https://github.com/cnjinhao/nana/pull/661)
    * [x] Ready on old repo
    * [x] Relevant for `v1.8-LTS`
    * [ ] Evaluate the general usage of `std::u8string_view` and if it shall removed from the repo.
    * [ ] Author contacted
    * [ ] Planed for `v1.8-LTS`
- [ ] [textbox focused border can now be disabled](https://github.com/cnjinhao/nana/pull/659)
    * [x] Ready on old repo
    * [x] Relevant for `v1.8-LTS`
    * [ ] Evaluate if integration of [Blue border around uneditable textbox](https://github.com/cnjinhao/nana/issues/656) shall be integrated
    * [ ] Author contacted
    * [ ] Planed for `v1.8-LTS`
- [ ] [Added support for setting arbitrary-format icons on Windows](https://github.com/cnjinhao/nana/pull/658)
    * [x] Ready on old repo
    * [x] Relevant for `v1.8-LTS`
    * [ ] Evaluate: `On that note I also wanted to say that the pixel buffer can be quite difficult to get pixel data from. Maybe the API could be improved in that regard.`
    * [ ] Code Review: 
        - `std::vector<uint8_t> pixels(size.width * size.height * 4);` to `uint8_t* pixels = new uint8_t[...];` (Check if this might be better to reduce memory footprint & allocations count)
    * [ ] Author contacted
    * [ ] Planed for `v1.8-LTS`
- [ ] [add listbox::items() method to get all items index_pairs](https://github.com/cnjinhao/nana/pull/613)
    * [x] Ready on old repo `Author(s) not convinced`
    * [x] Relevant for `v1.8-LTS` --> Maybe... say "Yes" for now...
    * [ ] Author contacted
    * [ ] Planed for `v1.8-LTS`
- [x] [Introduce command to share with menu and toolbar](https://github.com/cnjinhao/nana/pull/609) (Not relevant for `v1.8.0` we don't want to introduce new features. We can plan to use this for `v2.x`)

### Issues
- [x] #238 [macOS support?](https://github.com/cnjinhao/nana/issues/238) --> New feature --> Not in `v1.8-LTS` 
- [x] #240 [Custom listbox item renderer](https://github.com/cnjinhao/nana/issues/240) --> New feature --> Not in `v1.8-LTS` 
- [x] #241 [Scrollable place field](https://github.com/cnjinhao/nana/issues/241) --> New feature --> Not in `v1.8-LTS` 
- [x] #250 [Dynamic linking doesn't work](https://github.com/cnjinhao/nana/issues/250) --> CMake issue? --> Maybe in `v1.8.1`
- [x] #258 [Platform support?](https://github.com/cnjinhao/nana/issues/258) --> New feature --> Not in `v1.8-LTS` 
- [x] #266 [Callback for toolbar buttons](https://github.com/cnjinhao/nana/issues/266) --> New feature --> Not in `v1.8-LTS` 
- [x] #268 [the build directory is for building...](https://github.com/cnjinhao/nana/issues/268)
    * [x] Fixing: We are using conan and only cmake --> build directory removed
- [x] #269 [Make build process easier](https://github.com/cnjinhao/nana/issues/269)
    * [x] Done: Already partially fixed in `1.7.4`
    * [x] Fixing: We are using conan + cmake 
- [ ] #283 [Conan package](https://github.com/cnjinhao/nana/issues/283)
    * [x] Fixing: Conan is already used in this fork
    * [ ] Fixing: Final package version
- [x] #306 [textbox question](https://github.com/cnjinhao/nana/issues/306) --> New feature --> Not in `v1.8-LTS` 
- [x] #360 [listview?](https://github.com/cnjinhao/nana/issues/360) --> New feature --> Not in `v1.8-LTS`  (Maybe in `v2.x`)
- [ ] #372 [Bug in nana::group::div() when grid used](https://github.com/cnjinhao/nana/issues/372)
    * [ ] Evaluate if we will fix this
- [x] #376 [How to do smooth drawing with nana](https://github.com/cnjinhao/nana/issues/376) --> Wontfix --> NO
- [x] #394 [CMake - PNG library settings have no effect (missing include path/linker command)](https://github.com/cnjinhao/nana/issues/394)
    * [x] Fixing: Works with conan
- [x] #395 [list of widget names and their preview](https://github.com/cnjinhao/nana/issues/395) --> We will add proper documentation with `v2.x`
- [x] #396 [raw text input into textbox?](https://github.com/cnjinhao/nana/issues/396) --> New feature --> Maybe in `v2.x`
- [x] #401 [Generate pkg-config with cmake](https://github.com/cnjinhao/nana/issues/401) --> We use conan --> NO
- [x] #403 [Integrate with OpenGL](https://github.com/cnjinhao/nana/issues/403) --> Already fixed
- [x] #419 [Build errors with hotfix-1.7 branch using VS2017](https://github.com/cnjinhao/nana/issues/419) --> We will NOT continue developing `hotfix-1.7`
- [x] #434 [Compiler error when using boost filesystem](https://github.com/cnjinhao/nana/issues/434) --> We will drop boost support --> NO
- [ ] #436 [with every push to hotfix update branch develop](https://github.com/cnjinhao/nana/issues/436)
    * [ ] Make sure that we will grab all commits from `hotfix-1.7` and merge into new `main`
- [ ] #438 [CMake config support](https://github.com/cnjinhao/nana/issues/438)
    * [ ] Check conan CMake output
- [ ] #443 [Any suggestions for improving API?](https://github.com/cnjinhao/nana/issues/443) --> We might wanna implement some of the suggestions
    * [ ] Xeverous'1 : `widget::enabled() const` --> Fix / Add alternative
    * [x] Xeverous'2 : `button::enable_pushed` --> Agree but wontfix for `v1.8`
    * [ ] Xeverous'3 : `button::set_bground` --> Investigate
    * [x] Xeverous'4 : some names are not consistent with others --> Agree but wontfix for `v1.8`
    * [ ] Xeverous'5 : `button::transparent` --> Fix / Add alternative
    * [x] Xeverous'6 : `categorize` --> Agree but wontfix for `v1.8`
    * [ ] Xeverous'7 : `combox` --> Fix / Add alternative
    * [ ] Xeverous'8 : `progress` --> Fix / Add alternative
    * [x] Xeverous'9 : I don't get the API of progress bar --> Agree but wontfix for `v1.8`
    * [x] Xeverous'10 : `nana::API` --> Agree but wontfix for `v1.8`
    * [x] Xeverous'11 : `textbox` --> Wontfix for `v1.8`
    * [x] Xeverous'12 : `spinbox` --> Name if quit common... I see the point and don't like the name as well... But it is what is it... Maybe "NumericUpAndDown" (C#)... --> Wontfix for `v1.8`
    * [ ] aeonofdiscord'1 : `listbox` --> Investigate
    * [ ] 5cript'1 : `nana::filebox` --> We should consider it
- [x] #444 [make install rule not found](https://github.com/cnjinhao/nana/issues/444) --> We use conan now --> maybe consider it with #438
- [ ] #445 [crash on Windows upon startup](https://github.com/cnjinhao/nana/issues/445) --> Investigate
- [x] #446 [some examples are out of date](https://github.com/cnjinhao/nana/issues/446) --> We will redo docs on `v2.x`
- [ ] #450 [undefined behaviour - many violations of strict aliasing](https://github.com/cnjinhao/nana/issues/450) --> Investigate 
- [ ] #460 [crash on Linux on startup](https://github.com/cnjinhao/nana/issues/460) --> Investigate
- [x] #470 [fundamental types needs move constructors](https://github.com/cnjinhao/nana/issues/470) --> Not and issue / Wontfix
- [x] #476 [how to access the listbox item?](https://github.com/cnjinhao/nana/issues/476) --> Not and issue
- [x] #489 [Can I use cairo in nana for scientific plotting and visualization?](https://github.com/cnjinhao/nana/issues/489) --> Not and issue
- [x] #490 [Cannot build demo code(unresolved external symbol)](https://github.com/cnjinhao/nana/issues/490) --> Example will be rewritten an integrated in `v2.x`
- [x] #498 [1.7.2 Build failed on vs2019](https://github.com/cnjinhao/nana/issues/498) --> `v1.7.2` is outdated
- [x] #501 [Linking nana to exe and dll](https://github.com/cnjinhao/nana/issues/501) --> We will not support this usecase in `v1.8-LTS`
- [x] #506 [Stop supporting C++11/14](https://github.com/cnjinhao/nana/issues/506) --> We are already there
- [x] #508 [Some question about image processing](https://github.com/cnjinhao/nana/issues/508) --> New feature --> Not in `v1.8-LTS` 
- [x] #514 [Compile without Thread-local storage/callback support](https://github.com/cnjinhao/nana/issues/514) --> Not an issue / Feature not supported
- [ ] #516 [Support of high DPI](https://github.com/cnjinhao/nana/issues/516)
    * [ ] Check if HDPI is operation in dev
- [x] #520 [need examples for nana](https://github.com/cnjinhao/nana/issues/520) --> We will add proper documentation with `v2.x`
- [ ] #521 [listbox.column_movable(false) makes listbox columns also not resizable](https://github.com/cnjinhao/nana/issues/521)
    * [ ] Should be fixed: Validate
- [ ] #524 [Label documentation says url shouldn't work](https://github.com/cnjinhao/nana/issues/524)
    * [ ] Check if feature is implemented else implement it
- [ ] #525 [Question about menubar shortcuts](https://github.com/cnjinhao/nana/issues/525)
    * [ ] Validate if shortcuts work
- [x] #529 [filebox doesn't respect the DE single-click setting](https://github.com/cnjinhao/nana/issues/529) --> Wontfix / Not in scope of LTS
- [x] #533 [help with grouping widgets](https://github.com/cnjinhao/nana/issues/533) --> Not an issue
- [x] #534 [Add vcpkg installation instructions](https://github.com/cnjinhao/nana/issues/534) --> vcpkg will not be supported in LTS
- [x] #536 [Documentation Overhaul, perspective of a new user](https://github.com/cnjinhao/nana/issues/536) --> We will add proper documentation with `v2.x`
- [x] #538 [How to set the width of a single tab in the tabbar](https://github.com/cnjinhao/nana/issues/538) --> Not an issue
- [x] #540 [Suggestion to implement image rotation interface](https://github.com/cnjinhao/nana/issues/540) --> New feature --> Not in `v1.8-LTS` 
- [ ] #542 [animation does not work on multiple framesets](https://github.com/cnjinhao/nana/issues/542) --> Investigate
- [x] #546 [Transparent root window](https://github.com/cnjinhao/nana/issues/546) --> New feature --> Not in `v1.8-LTS` 
- [ ] #548 [spinbox with double value shows too many zeros](https://github.com/cnjinhao/nana/issues/548)
    * [ ] Check if feature is implemented else implement it
- [ ] #553 [Why do textbox::set_keywords works only with std::initializer_list?](https://github.com/cnjinhao/nana/issues/553)
    * [ ] Check if feature is implemented else implement it
- [x] #556 [how can i setup a fix width button in demo http://qpcr4vir.github.io/nana-doxy/html/d3/de9/widget_show_8cpp-example.html](https://github.com/cnjinhao/nana/issues/556) --> Not an issue
- [x] #557 [How to build on OpenBSD](https://github.com/cnjinhao/nana/issues/557) --> Not in `v1.8-LTS` 
- [x] #561 [Thank you to contributors](https://github.com/cnjinhao/nana/issues/561) --> Not an issue
- [x] #562 [Highlighting code in nana](https://github.com/cnjinhao/nana/issues/562) --> New feature --> Not in `v1.8-LTS` 
- [x] #565 [Linux build fails](https://github.com/cnjinhao/nana/issues/565) --> We will get working build on Linux with `v1.8-LTS` and conan 
- [x] #578 [Dark grey is lighter than grey](https://github.com/cnjinhao/nana/issues/578) --> Fixed
- [ ] #579 [Menubar/Menu display problem in develop-1.8](https://github.com/cnjinhao/nana/issues/579)
    * [ ] Check if bug is fixed
- [ ] #581 [text line disappears in textbox when pressing BACKSPACE or DEL](https://github.com/cnjinhao/nana/issues/581)
    * [ ] Check if bug is fixed
    * [ ] Check if mentioned crash is rly a thing and fix it
- [ ] #583 [request combox to support key select](https://github.com/cnjinhao/nana/issues/583)
    * [ ] Check if feature is implemented else implement it
- [x] #584 [old documentation](https://github.com/cnjinhao/nana/issues/584) --> We will add proper documentation with `v2.x`
- [ ] #592 [combox::clear() does not clear the textbox in combox](https://github.com/cnjinhao/nana/issues/592)
    * [ ] Check if bug is fixed else fix it
- [ ] #595 [how to draw text on pixel_buffer](https://github.com/cnjinhao/nana/issues/595) --> Investigate if easy fixable (BitBlend from font data, ...) see if it's practical to do...
- [x] #597 [spinbox edit box does not track allowable values](https://github.com/cnjinhao/nana/issues/597) --> Not an issue
- [x] #601 [Building shared library fails on Ubuntu 20.04](https://github.com/cnjinhao/nana/issues/601) --> We will use conan and is already fixed in dev
- [x] #611 [Compilation error](https://github.com/cnjinhao/nana/issues/611) --> Not an issue
- [x] #616 [new feature of toolbar](https://github.com/cnjinhao/nana/issues/616) --> I will already check
- [x] #617 [need help installing NANA](https://github.com/cnjinhao/nana/issues/617) --> Not an issue
- [x] #618 [Internationalization - comments are not supported in PO translation files](https://github.com/cnjinhao/nana/issues/618) --> Fixed
- [x] #622 [opencv mat and nana::image](https://github.com/cnjinhao/nana/issues/622) --> Not an issue
- [ ] #623 [Wondering about the new units (px and em) introduced into develop-1.8](https://github.com/cnjinhao/nana/issues/623)
    * [ ] Fix HighDPI issues
- [ ] #624 [treebox::clear failed](https://github.com/cnjinhao/nana/issues/624)
    * [ ] Check if bug is fixed else fix it
- [x] #629 [Insert widget into specific position in place's field](https://github.com/cnjinhao/nana/issues/629) --> Not an issue / New feature
- [x] #630 [messagebox icon doesn't appear when path has unicode characters](https://github.com/cnjinhao/nana/issues/630) --> We will not support this usecase in `v1.8-LTS`
- [ ] #631 [API::emit_event behavior is different from a "real" event](https://github.com/cnjinhao/nana/issues/631) --> Investigate
- [x] #634 [why can not use in vscode?](https://github.com/cnjinhao/nana/issues/634) --> Not an issue
- [x] #641 [Hello guys! Can I make a brand new installation guide for your library?](https://github.com/cnjinhao/nana/issues/641) --> We will add proper documentation with `v2.x`
- [x] #652 [M1 compilation error](https://github.com/cnjinhao/nana/issues/652) --> New feature --> Not in `v1.8-LTS` 
- [x] #656 [Blue border around uneditable textbox](https://github.com/cnjinhao/nana/issues/656) --> Related PR already in review
- [x] #660 [nana::menu custom renderer gives garbage std::u8string_view input](https://github.com/cnjinhao/nana/issues/660) --> Related PR already in review
- [ ] #663 [Needed: ability to change tooltip and scrollbar colors, listbox custom renderer](https://github.com/cnjinhao/nana/issues/663)
    * [ ] Implement
- [x] #668 [attaching tags to widgets to distinguish widgets in event handlers](https://github.com/cnjinhao/nana/issues/668) --> New feature --> Not in `v1.8-LTS` 
- [x] #669 [Android](https://github.com/cnjinhao/nana/issues/669) --> New feature --> Not in `v1.8-LTS` 
- [x] #670 [fatal error: nana/gui/wvl.hpp: 没有那个文件或目录](https://github.com/cnjinhao/nana/issues/670) --> Not enough information
- [x] #672 [Integrate nana with Directx](https://github.com/cnjinhao/nana/issues/672) --> Already Fixed (OpenGL) / New feature --> Maybe in `v2.x`
- [x] #674 [Build error with C++20 standard](https://github.com/cnjinhao/nana/issues/674) --> We will use conan for `v1.8-LTS`. We will make sure everything works.
- [x] #675 [Finally a conan package (Soon)](https://github.com/cnjinhao/nana/issues/675) --> Not an issue
- [x] #676 [State of the lib/repo. Is this still actively maintained?](https://github.com/cnjinhao/nana/issues/676) --> Not an issue
