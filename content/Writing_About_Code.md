title: Writing About Code: Getting Started
date: 2013-09-27
category: writing
tags: tech writing, tutorial
summary: Writing code is job one for most software developers, but learning to write *about* code is almost as important. Notes from a presentation I gave on writing about code.


Writing code is job one for most software developers, but learning to write *about* code is almost as important. Whether you're documenting an API or showing off your own smarts, when you set out to write about what you think you know, it tests how well you really know the subject.  As you write, you'll often end up deepening your understanding of how the code works and honing your skills as a developer.

In this post I'm going to provide some tips and tricks for programmers who haven't done much writing that will help you get started and find early success that fuels more writing.

This is a distillation of the first part of my "Writing About Code" presentation at [Vermont Code Camp 2013](http://vtcodecamp.org/). I don't believe dumping my slides on the web helps. Instead, I'm pulling the most important ideas from my presentation into a few blog posts that are easier to read, digest and use to fuel your own work.

## Why write about code?

There are many reasons to write about code. Maybe you want to share your knowledge and enthusiasm for programming, to market a product or teach customers how to use it, to promote your own abilities or because it is (or should be) part your job.

But I'd like to suggest another, more valuable reason, best summed up in this ancient wisdom from Seneca the Younger: *Docendo discimus* ("by teaching, we learn").

Whether you write for yourself or decide to write publicly, you’ll start to explain something and, often as not, start wondering: Really? Is that all there is to it? What am I missing? How does this work? Engineers — your target audience — are always going to point out edge cases and pedantic details. Are you ready?

Go ahead and second guess your assumptions about your code, dig into the how and the why. You will most likely learn something new and improve your skill as a developer.

## My code speaks for itself, right?

Unfortunately, your code does not speak effectively for itself — not for a wide audience anyway.

A code example does not replace an explanation. Sure, there are times when sharing a simple code snippet seems sufficient, but even then it's usually posted in the context of a discussion... usually via social media.

If you show code you should explain the code, even if it seems obvious to you. You wrote it, so of course it's obvious. But there are many other people — your potential readers — who are trying to learn. If the concepts you present in your code were obvious, these people wouldn't need to be reading about it.

Many of your readers are going to be far less accomplished programmers. Believe it or not, by simply taking the time to research and write a blog post, you become an expert. Help them understand.

In fact, this is where a lot of official documentation falls down. It shows the most basic example, but frequently fails to take it farther than that. Then it expects you to jump straight to a complete sample app. There's often little explanation of how you get from A to Z.

You may think it's all be written before. What do you have to contribute? We're still figuring this programming thing out. Every bit of knowledge helps move the profession forward. People are still writing about C. People are still writing about Cobol! Your unique approach to the subject may be the key that unlocks a problem for some reader.

## Fear of writing... or how I learned to stop worrying and just write

The most important tip: Write something.  Anything. Just get it out of your head and on the screen. Make time to write every day. 100 words or 30 minutes or whatever seems achievable on a regular schedule. As you become more comfortable, try increasing your target time or word count.

Do make it a habit, but don't make it a chore. If you get stuck, stop and come back to it later.

Use the tools and languages you use every day. Write about the thing on your  mind right now. A distraction that often gets in the way of writing (and probably coding, too) is obsessing over the "best" tools. There is not best writing tool, and messing with different editors just keeps you from writing. Word is fine, but so is a basic text editor... your IDE will probably work fine if that's where you're most comfortable and productive.

Don’t underestimate the usefulness of pencil and paper.

A helpful approach for avoiding editorial paralysis is to commit yourself to at least two trips through the material. I think most people get in trouble by trying to edit while they write. The result is usually not writing. An outline or a list of the major points you want to touch on works well, but from that starting point, try to write stream-of-consciousness. Get as much down on paper as possible.

Don't fixate on the entire article. Work idea by idea, section by section. Each sentence is a building block for a paragraph, and each paragraph is a building block for your article.

Although correct technical details are important, as are correct spelling and capitalization, don't get hung up on researching each topic as you write. If there's something I'm not sure about or that needs more detail, I prefer to make a note to myself inline to go back and double-check or add more information later. Better to have the sketched out skeleton of your writing in place rather than getting side-tracked by research from writing at all.

Write a *complete* first draft before making any edits or revisions. That includes fretting about spelling, grammar, and so on. Once that draft is complete, *then* read it through, fix mistakes, add details, re-order, refine, and refactor as needed.

## Focusing your big ideas into byte-sized pieces

A common problem for writers is determining the scope of what you're going to write about. If the idea is too big, you're likely to run into two problems: You either never finish (which is frustrating) or you skip over important details to finish (which leads to a poor finished product).

At least when you're starting out, focusing your writing on small, achievable goals will help you succeed more often, giving you confidence in your writing and setting up a positive feedback loop of writing, accomplishment and more writing.

It's often better to focus in on a very specific detail and write about that as clearly as possible. You have a more clear goal for the writing in front of you. You can often think around the smaller concepts more easily. Plus, there's less to write — you'll finish more quickly.

You can stitch together other small, focused bits of writing into episodic blog posts ([Oren Eini](http://ayende.com/blog) does this very effectively on his blog) or into a longer article.

You’ll often find that small topics aren’t really so small when you dig into them. Think about not just how you implement a solution, but how it works... and why. What are the edge cases? What’s helpful to know? How much is boilerplate, implemented for you by the IDE or framework? Can you explain how *that* all works? How much is "received wisdom" about how things should be done, or code IntelliSensed in with a keystroke?

In fact, I suggest, as an exercise to practice writing about your code: take a chunk of code and explain it block by block. I bet you'll discover quite a few assumptions you've made along the way. It doesn't have to be your code. Document some random source code just for the practice.

Avoid pasting in large code blocks. It hinders the flow of reading and distracts your reader while she deciphers the entire block. Instead, break your code into digestible snippets if at all possible. Explain each bit as you go through.
At the end you can provide the entire code block for copying and pasting, or link to a file/repo.

I suggested digging into the details, but you don't always have to explain how deep the rabbit-hole goes. Most of the time, unless you're writing basic programming tutorials, you shouldn't have to explain how a for loop works, or what you're iterating or basics like that.

Instead, think about the conceptual building blocks of your idea. Break code down into snippets that let you discuss it in terms of those building blocks. For nuts and bolts coding, that may mean discussing code line by line within individual methods. Other times you might discuss the overall construction of an entire class (suitably simplified, if possible) or of classes within an application.

As an example, take a look at Chris Eidhof's [Lighter View Controllers](http://www.objc.io/issue-1/lighter-view-controllers.html) article at objc.io, which examines code organization at the class and file level. Then consider Peteris Krumins' [Bash One-Liners Explained](http://www.catonmat.net/blog/bash-one-liners-explained-part-one/) series of posts, which by definition examines one line of code at a time in great detail.

## What to write about?

Still not sure where to start? Here are a few ideas:

* Write about what you’re enthusiastic about
* Write about what you’re curious about
* Write about what you’ve done that makes you feel smart
* Write about a problem you had to solve
* Write about what annoys you or makes you smile
* Write about what you don’t understand: you’ll learn along the way<p>

There is a audience out there eager to learn. Start writing for them. It will do you some good, too.

People love to learn how things work... and why.

People love when someone else solves their problems.

People want to know what they need to know and where to find it. They want to know how to get started, and then they need to be handheld from the simple to the more complex.

People always appreciate clever and useful utilities and code snippets, and tips for how to use them.

## Stop reading, start writing

You have some basic tools for getting started. Now put them to work and get started writing something every day. You don't have to publish it. Just keep a journal for practice... a journal of ideas, which you might return to later for material as you become more confident in your writing.

Now, get writing...