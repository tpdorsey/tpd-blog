title: Sublime Text 3 Setup
date: 2014-11-17 22:05:00
category: programming
tags: tech, sublime text, editors, note to self
summary: This is how I set up Sublime Text 3 for both coding and technical writing.


**Note: I've mostly moved on to Visual Studio Code, but still find Sublime Text useful and always have a copy installed.** 

I recently had to set up [Sublime Text 3](http://www.sublimetext.com/3) all over from scratch due to reasons of not planning ahead. It seemed prudent to write the steps all down for future reference and put the whole thing where I wouldn't loose it. Like on my blog.

Nothing fancy, but it works for my purposes.

Start out by installing [Package Control](https://sublime.wbond.net/installation), the package manager for ST2 and ST3.

Open the command palette with CMD+Shift+P (Ctrl+Shift+P on Windows) and run **Package Control: Install Package** to find and install packages. See the Package Control [Usage](https://sublime.wbond.net/docs/usage) page for instructions on the process. Generally I like to search for packages on the Package Control site first so I can check for version compatibility, dependency gotchas and evidence of abandonware.

[Markdown Extended](https://sublime.wbond.net/packages/Markdown%20Extended) is my preferred Markdown implementation. I actually set up ST3 to ignore the default Markdown package as you can see in the preferences below.

I'm using [Monokai Extended](https://sublime.wbond.net/packages/Monokai%20Extended) as the theme just for Markdown Extended. Again, see the preferences JSON below. There was some monkey business involved in getting this set up, unfortunately: I had to use [PackageResourceViewer](https://sublime.wbond.net/packages/PackageResourceViewer) to extract Monokai Extended into my /Packages folder, then point to that .tmTheme file (again, see below). This works better on my work machine, so I'll have to double-check that setup and report back any further information. For now it's good enough to get working.

I'm also using [Colorcoder](https://sublime.wbond.net/packages/Colorcoder) for semantic code coloring. It looks like Ruby support is installed by default now. Previously I had to use a workaround discussed in [this issue on GitHub](https://github.com/vprimachenko/Sublime-Colorcoder/issues/20).

When installed you can now just go to View > Syntax > Colorcoder > Ruby (Colorcode). Colorcoder also has built-in support for C++, Coffeescript, Go, Lua and Python.

[Pretty JSON](https://sublime.wbond.net/packages/Pretty%20JSON) is a good package for formatting and minifying JSON. I find it helpful, along with [JSON Formatter](https://github.com/callumlocke/json-formatter) for Chrome.

I don't need to do diffs often, but when I do, [Sublimerge: The professional diff and merge tool for Sublime Text 2 and 3](http://www.sublimerge.com/) is the way to go. Buy it and support a developer who makes a really nice, useful tool.

As mentioned earlier, I'm using Monokai Extended as my Markdown-specific theme. Colorcoder applies semantic coloring, but it does so in conjunction with your existing theme setting. For general coding, I'm using [PlasticCodeWrap](http://tmtheme-editor.herokuapp.com/#/theme/PlasticCodeWrap), which I grabbed from the terrific [tmTheme Editor](https://github.com/aziz/tmTheme-Editor) by Allen Bargi.

And that's pretty much it for my ST3 setup. My work setup has [SublimeLinter 3](http://www.sublimelinter.com/en/latest/#) installed, but I don't end up using it much.

## Keybindings

I also don't do much in the way of fancy keybindings. However, here are two that I've found useful.

```
[
  { "keys": ["super+k", "super+t"], "command": "title_case" },
  { "keys": ["ctrl+alt+super+m"], "command": "set_file_type", "args":{ "syntax" : "Packages/Markdown Extended/Syntaxes/Markdown Extended.tmLanguage" } },
    { "keys": ["ctrl+alt+super+t"], "command": "set_file_type", "args":{ "syntax" : "Packages/Text/Plain Text.tmLanguage" } }
]
```

The first keybinding creates a shortcut for Title Case, which doesn't have a default keybinding. The shortcut is CMD+K, then CMD+T, which follows the same pattern as the Upper Case and Lower Case bindings.

The second keybinding toggles between text and Markdown syntaxes for the current file. Mostly this is handy for .txt files that contain Markdown. I noticed, however, that this must be a keybinding I originally created for ST2. Package locations have moved around a bit since then. I had to unpack the Markdown Extended package with PackageResourceViewer and point the keybinding to the unpacked tmLanguage file. There must be a better way.

## Preferences

Here's my current Markdown Extended.sublime-settings. This is where I set the a default theme for the syntax that's different from the general theme.

```
{
  "color_scheme": "Packages/Monokai Extended/Monokai Extended.tmTheme",
  "margin": 100,
  "wrap_width": 80
}
```

And here are my general user preferences. I use [Inconsolata](http://levien.com/type/myfonts/inconsolata.html) at a sane size for mature eyes on large or Retina displays. Tabs are two spaces as the goddess intended. You can also see here that I ignore the default Markdown package.

```
{
  "color_scheme": "Packages/Colorcoder/PlasticCodeWrap (Colorcoded).tmTheme",
  "font_face": "Inconsolata",
  "font_size": 17,
    "tab_size": 2,
  "translate_tabs_to_spaces": true,
  "trim_trailing_white_space_on_save": true,
  "ignored_packages":
  [
    "Vintage",
    "Markdown"
  ],
  "original_color_scheme": "Packages/Monokai Extended/Monokai Extended.tmTheme"
}
```

I'm not obsessive about fixed-width fonts. Check out Dan Benjamin's [Top 10 Programming Fonts](http://hivelogic.com/articles/top-10-programming-fonts) and follow-up posts for some excellent suggestions. Adobe's [Source Code Pro](https://github.com/adobe-fonts/source-code-pro) is nice if you don't mind having Adobe software on your system.

That's about it for setup. The magic is in the writing and the coding.