title: Markdown Links with Template
date: 2014-07-16
category: Writing
tags: Tech, Tools
summary: The Template extension for Chrome is a highly customizable utility for extracting data from a web page to the clipboard in a single action.


In [Dr. Drang's](https://twitter.com/drdrang) recent blog post, [Quicker Markdown linking with TextExpander](http://www.leancrew.com/all-this/2014/07/quicker-markdown-linking-with-textexpander/), the good Doctor takes a five-step, [TextExpander](http://smilesoftware.com/TextExpander/index.html)-powered workflow for creating Markdown-flavored links created by [David Sparks](http://macsparky.com/) (of [Mac Power Users](http://www.macpowerusers.com/) fame and notoriety) and improves it with a new, streamlined TextExpander snippet fueled by 18 lines of AppleScript.

The Dr. Drang version programmatically retrieves the URL of the current page in either Safari or Chrome and creates a Markdown link with it. The upside of this method is that you can create a Markdown link without having to switch between apps. The downside is that the web page has to be in the currently selected tab in either Safari or Chrome and you have to supply the link text.

It's a neat solution. In theory it saves you a context swap between editor and browser, and Dr. Drang's script is also an interesting starting point for much deeper customization. But I'd like to point out what may be an even better option.

## Template Extension

The [Template](http://template-extension.org/) extension for Chrome is a highly customizable utility for extracting data from a web page to the clipboard in a single action.

The key feature is Template's built-in templating language the enables you to create custom actions that can extract just about anything directly associated with a web page or browser: page URL and title text, meta information in the page, links for all current tabs in the browser and a whole lot more. Check out the [Guide](http://template-extension.org/guide/) for details about all of the template tags and operations you can use.

You can execute any of the templates set up in the extension via a toolbar menu, a right-click context menu or, optionally, a user configurable, template-specific keyboard shortcut.

I've only touched the surface of what Template can do, but it hugely simplified many aspects of my work as a technical writer, particularly when it comes to capturing research notes or sharing links. Template has become one of those must-have, first install tools, alongside [Alfred](http://www.alfredapp.com/), [Sublime Text 3](http://www.sublimetext.com/3) and TextExpander.

I'll give you a few examples of Template in action just to give you an idea of what's possible.

## Using Template

The simplest template I use regularly just grabs the title of a web page and the URL, something I might grab to paste into an email or Tweet. The template tags are simply `{title} {url}` and it returns simple strings like so:

```
Bash $PS1 Generator 2.0 https://www.kirsle.net/wizards/ps1.html`
```

A similar one creates a simple Markdown link using the `[{title}]({url})` tags. The results look like this:

```
[Bash $PS1 Generator 2.0](https://www.kirsle.net/wizards/ps1.html)`
```

Template includes a built-in `{selectionMarkdown}` tag that takes any text you've selected from the page and does some simple Markdown conversion of elements such as links, emphasis, strong and so on. Here's an example:

```
Still, [as Marvin and Tammi say](https://www.youtube.com/watch?v=svAs-6MiqxE&feature=kp), ain't nothing like the real thing, baby.`
```

I haven't tested this extensively to see what breaks the encoding, but it meets my limited expectations.

There's also a `{selection}` tag that just grabs the selected text. I use this, along with the title, URL and a blockquote prefix, for research notes with an attribution.

```
> {selection} From: [{title}]({url})`
```

So I just select some text, invoke the Template action, then paste:

> This works, but… blech. There’s a better way. From: [Quicker Markdown linking with TextExpander - All this](http://www.leancrew.com/all-this/2014/07/quicker-markdown-linking-with-textexpander/)

There are some limitations here.

First, it requires Chrome. That's fine for me, but you may prefer another browser. (I keep Firefox around just for those moments when I need [TableTools2, the Firefox extension that Sorts, Searches, Summarizes, Filters, Copies, Charts, Rearranges, Combines and Compares HTML Tables!](http://www.mingyi.org/TableTools2/))

Second, it requires going to the browser tab I want to copy from, which is a context switch specifically avoided by Dr. Drang's script. I find this an acceptable compromise &mdash; generally I'm already looking at the tab when I want to grab a link or other data from it, *then* switching over to the editor in which I want to use the results. Your mileage may vary.

I've used all of, what... four of the built-in tags here, and none of the available operators. There's just a ton of potential in Template. It's in no way a replacement for TextExpander, but it is another incredibly handy arrow in the quiver.

And now that I think about it, some pretty interesting things could be done with Template *and* TextExpander together to extract elements of a page, place them on the clipboard, then paste them with additional formatting or cursor placement via a snippet and some script. Hmmm....