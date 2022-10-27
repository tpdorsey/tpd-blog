title: Teaching Kids Programming With RubyStory
date: 2014-01-22
category: Programming
tags: Tech, STEM, Ruby
summary: I wrote some course materials and sample code for teaching the basics of Ruby programming to middle-school kids. The course is called RubyStory and it teaches just enough Ruby to create a choose-your-own-adventure style storytelling game.


TL;DR version: I wrote some course materials and sample code for teaching the basics of Ruby programming to middle-school kids. The course is called [RubyStory](https://github.com/tpdorsey/RubyStory) and teaches just enough Ruby to create a choose-your-own-adventure style storytelling game.

![RubyStory]({static}/images/RubyStory.png)

<hr>

Last year my older daughter started fifth grade and brought home a school-supplied MacBook. Which is great. I think it's important to give kids a chance at an [early head start](http://www.avc.com/a_vc/2013/12/girls-who-code.html) to develop technology and programming skills — an early taste, anyway, to see if they like it — [particularly the girls](http://www.codeproject.com/Articles/542465/CodeProject-Advisory-Board-for-Women-in-Technology).

I set about looking for an appropriate learning resource to teach my daughter. There's a lot out there. Unfortunately, none of it quite appealed to my preferences.

I wanted something easy for me to read, parse out what was being taught, and know what to pass on to students. Many of the course materials I reviewed required a lot of up-front reading, then I'd have to create my own teaching notes.

Adults and older children might be motivated to learn programming for its own sake, but I think younger kids (8-13 at least) don't have the same motivation (exceptions discussed below).

Learning while doing something fun, however, seems to work. So I wanted to start with an interesting goal and make sure each step along the way was both educational and fun.

Finally, the laptops at my daughter's school are locked down, so I needed something that required no software not already installed on the machines.

Ultimately, it seemed easier to create my own materials. As a bonus, as mentioned in my posts about [writing about code](http://www.terrencedorsey.com/2013/09/27/Writing_About_Code.html), I'd probably learn a lot in the process. And I did.

## RubyStory

The result is a course I wrote called [RubyStory](https://github.com/tpdorsey/RubyStory) and you can grab all of the materials from Github. The details are covered in the readme.

The course materials are intended for teaching *to* kids. I suppose they could be used for self-instruction, but my assumption is that kids who are ready and motivated to learn programming on their own are probably also ready and motivated enough to learn from a book or a more traditional tutorial.

I recommend Zed Shaw's [Learn Python The Hard Way](http://learnpythonthehardway.org/) and Rob Sobers' [Learn Ruby The Hard Way](http://ruby.learncodethehardway.org/). Both influenced the storytelling aspect of RubyStory.

The RubyStory materials are intentionally sparse. There's an outline and sample code and handouts. There's a slide deck, but it's mostly just to show the code examples, which students can then type on their own.

The outline provides a concise overview of the topics to teach, but be prepared to fill in details, answer questions and riff a bit as your students require.

I wrote this course with the assumption that the teacher already has some basic programming knowledge. You don't need much:

* Creating and using variables
* Strings and integers
* Basic math and Boolean logic
* Printing messages to the terminal
* Capturing input from the command line
* If statements
* Functions

That's all we use. Even if you know nothing about Ruby, you should be able to pick it up quickly. (*I* knew almost nothing about Ruby before starting this project.)

## Why Ruby?

As you can tell from the minimal set of programming concepts covered by RubyStory, it's hardly language specific nor does it really "teach Ruby." In this case, Ruby is a convenient tool.

First, Ruby is already installed on every recent MacBook. The version installed is not important.

We don't need any special tools to program with Ruby, just Terminal and a text editor. TextEdit isn't the tool I'd prefer — syntax coloring would be a nice feature — but we can live with it for simplicity. (The slides do include syntax highlighting.)

Ruby has very simple syntax and very little necessary punctuation. Whitespace and semicolons aren't that important and there are very few parentheses and brackets to worry about. I've found that kids have enough trouble with accurate typing. Simple syntax makes troubleshooting much easier.

Plus, I wanted to learn some Ruby. And I did.

## Next Steps

Please fork the RubyStory repo and give teaching a try. I am continually updating the materials as I teach and learn from the kids — what the enjoy, what they build, what questions they ask, where I can help them go next. Let me know what you learn while teaching with RubyStory.

As written, RubyStory should be easily adapted to Linux systems, but I haven't yet into what additional material would be needed for Chromebooks or Windows. It's on my to do list.

Other than that, I'm now focused on using RubyStory for teaching in my community. I hope you will, too.