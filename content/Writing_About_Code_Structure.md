title: Writing About Code: Structure
date: 2013-09-30
category: writing
tags: tech writing, tutorial
summary: Many of us were taught a five-paragraph mode of construction: tell us what you're going to tell us, tell us, then tell us what you told us. This is boring, repetitive, and evil. More notes from a presentation I gave on writing about code.


In my previous post, I provided some tips about [how to get started writing]({filename}/Writing_About_Code.md). That's all well and good, but you would probably also appreciate some tips on what to write and how to organize your writing into something coherent and readable. Let's dig into that now.

Many of us were taught a five-paragraph mode of construction: tell us what you're going to tell us, tell us, then tell us what you told us. This is boring, repetitive, and evil. Don't do it.

Instead, consider this structure for your writing:

1. Problem
2. Solution
3. Next steps

It's similar to the old five-paragraph model — there's an introduction, a body and a conclusion — but I think this structure better directs the organization of your writing and makes for more interesting reading.

## The problem statement

The problem statement is the introduction. It serves two purposes. First, it explains briefly what your article is about. Second, it's your opportunity to grab the reader's attention.

Starting with the second point, many readers think being outrageous or funny makes for a good hook. While that *can* work, it throws an unnecessary variable into the equation. Are you really funny? Is that enough to hook a reader? Are you sure?

Maybe it's better to just clearly state what you're writing about. Provide some context: what does it relate to (language, platform, type of development...), and why should I care (am I doing it wrong, does this make my code faster, stronger, less buggy...)? This is why I called it a "problem statement."

Readers are often more interested when you clearly define your subject within a the scope of a problem they might encounter and one or more solutions that solve the problem. One approach, of course, is to literally solve a problem, but taking a more abstract view of the problem-solution structure can help guide your writing on other topics as well.

Keep your introduction brief, but it can be several paragraphs if necessary to set up the context in sufficient detail. However, make sure at least one paragraph — preferably the first or last paragraph of your introduction — clearly states what your entire post is about. People who will share your article in social media, aggregators, and newsletters will cut and paste. Make it easy for them.

Here's a good example of a brief and to-the-point introduction in an article by [Chris Eidhof](http://twitter.com/chriseidhof) on [Lighter View Controllers](http://www.objc.io/issue-1/lighter-view-controllers.html).

> View controllers are often the biggest files in iOS projects, and they often contain way more code than necessary. Almost always, view controllers are the least reusable part of the code. We will look at techniques to slim down your view controllers, make code reusable, and move code to more appropriate places.

Notice that, in three sentences, Chris explains the context (view controllers in iOS programming), the problem (they're too big and not reusable) and what he's going to explain (a solution for slimmer, more reusable view controllers).

Here's a longer example from [Charles Petzold's](http://www.charlespetzold.com/) [DirectX Factor](http://msdn.microsoft.com/en-us/magazine/dn385714.aspx) column in MSDN Magazine.

> High school geometry comes in two distinct flavors: Euclidean geometry is oriented around constructions, theorems and proofs, while analytic geometry describes geometric figures numerically using points on a coordinate system, often called the Cartesian coordinate system in honor of the pioneer of analytic geometry, René Descartes...

> In the previous installment of this column... I discussed how to use the ID2D1PathGeometry to render lines in a finger-painting application that runs under Windows 8. Now I’d like to step back and explore geometries in broader detail, and in particular investigate some of the intriguing methods defined by ID2D1Geometry for manipulating geometries to make different geometries.

This is a longer introduction, and I've even left out a paragraph for clarity, but you can see that it includes the same building blocks: a context (geometry in Windows 8 programming, continuing from a previous articles), a problem (geometry is hard, you need to know how it works), and a solution (learn about ID2D1Geometry).

If you can keep your introduction — your problem statement — focused like this, it will help you keep the rest of your article focused as well.

## The solution

This is the meat of your article and where you'll spend the most time writing. I won't spend too much time on this as it's really the focus of [my first post on getting started writing]({filename}/Writing_About_Code.md). You just need to pick a subject and start writing.

The main portion of the article is where you can explain the problem or opportunity in more depth than a concise intro problem statement allows. Stop and provide some more context if necessary, though don't let it distract from getting to the solution. If the problem starts to become the entire article, you might want to rethink what the article is about. Maybe that's another writing project altogether, or maybe you can link to more context elsewhere.

How you write about your "solution" depends on subject and the way you want to organize your ideas. A few common patterns are:

* Start from the beginning and work through to solving the problem
* Pick a few key elements to explain
* Top ten lists (pro tip: odd numbers work better)
* Analysis of different patterns or implementation approaches
* Pros and cons

There's not necessarily a right or wrong way to organize the core of your writing. Go with your gut, pick something, and run with it. After you complete a draft, if the organizing theme you've selected doesn't seem to be working, don't try to force it. Rather, be open to refactoring and heading in a different direction. Reorganizing takes less effort than re-writing.

## Next steps

I'm of the opinion that a blog post or article does not, in fact, require a formal conclusion. If you finish your subject and want to simply stop, that's fine.

This is particularly true of very short blog posts that cover a single, very focused subject. Provide some context and a problem statement, explain yourself through your solution, and done!

If you do want to provide some closure, don't simply restate your original thesis. Instead, you can just sum up quickly: "That's a quick overview of recursive dohickies in action."

Another approach, if there are other considerations, is to qualify your solution. Although I've warned against pedantic, edge-case addicted readers, you don't need to be all-inclusive or all-encompassing in your solution. Just explain that there's more to the subject: "This solution works well for most apps, but edge cases X, Y, and Z require additional hemming and hawing." Maybe that's fodder for future writing.

As implied by my heading, it's always helpful to suggest some next steps for the reader: where to learn more or find additional examples. Other potential solutions or associated technologies. Ideas for further or more sophisticated implementations. You don't need to go on at length. A simple mention and, perhaps, a link goes a long way.

## Use links to your advantage

Links are the lifeblood of the web, and links in your article are good. They let you pull related context and information into your post without having to write it. They also let you recommend quality sources of information and code to your readers, situating your own writing within the larger web of discussion on the subject.

You can (and should) link to your own previous posts. Go back and add links in previous posts if you cover the subject again later. This is particularly important for multi-part series of articles so a reader can find the beginning of the series from any post in the series, then follow through from the end of one post to the beginning of the next. If you make it easy for readers to stay on your site, they will.

Link to other people's posts if they're relevant and helpful. People (readers and writers) appreciate that, and if they've already covered a subject, it saves you from repeating it.

Link to apps, libraries, reference material and anything else that you use or discuss in depth so readers can find and use it too. Make sure you get the name right, though, and it's a nice touch if you check occasionally that links still work.

## Comments on the code examples

Code is great. You should definitely include code examples if they're relevant to in your writing. But a code example does not replace an explanation.

If you show code, you should explain the code, even if it seems obvious to you. You wrote it. Of course it's obvious. However, your reader is trying to learn. If it was obvious, they wouldn't be reading... and many of your readers are going to be far less accomplished programmers than you. Help them understand.

In fact, this is where a lot of official documentation falls down. It shows the most basic example, but never take it farther than that. Then it jumps straight to a complete sample app. There's often little explanation of how you get from A to Z.

And as we know, the API is rarely as straightforward to use as the author thinks. There are always inconsistencies and gotchas and misnamed features and things that look the same but do something completely different.

You don't need to show all of your code if it's available somewhere else. Just the important or interesting bits, and a link to peruse the rest.

If there are dependencies, make them clear.

Test your code in a fresh environment (VM maybe) to double-check that there are no unexpected dependencies. "It works on my machine... " is never a good excuse.

The specific coding style choices you make are not as important as consistency and clarity. Pick something and keep with it. It can help to use super-clear naming that you might not use in real code.

Now, get writing...