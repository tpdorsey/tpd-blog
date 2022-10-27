title: Coding in Public
date: 2012-11-01
category: Programming
tags: Tech, Opinion
summary: Posting code to GitHub and my first pull request.


I recently wrote a bit about [customizing archive creation](/2012/08/10/Updates_to_the_Archives/) in the staticDimension blog engine I use. In the process, I also created my first [Github repo](https://github.com/tpdorsey/staticDimension) for my fork of the staticDimension codebase.

Bonus: Mike Wats merged my pull request, and now the new archive code is part of the core [staticDimension code](https://github.com/MalphasWats/staticDimension) on Github.

Not bad for a first attempt at coding in public.

I've been working with developers and writing or editing articles about software development for a long time. But here's a confession: over all those years I never really learned to code properly. Sure, there was the occasional script, or picking up a book on C or JavaScript or whatever folks were writing about at the time.

But it never really clicked for me. Until this year, when I started to put some real effort into not just learning about coding, but actually putting fingers to the keyboard and making something — anything! — execute and do something — anything!

I'll write a bit more about the experience of putting years of theory into action another time. Right now I'm going to share my experience of doing one of my first real coding projects, however small it may be, right out in public for everyone to see.

## The Basics

As I mentioned in the [previous post](/2012/08/10/Updates_to_the_Archives/), my primary goal for this project was to create a simpler, easier to navigate archive of my blog posts that no longer appeared on the home page. Simple solution: create a single page with a listing of past posts. In the unlikely event that someone wanted to find one of my old posts, it would be easy to simply go to the archive page and either scroll the list or Command-F find the desired post title — responsibilty on me to write relevant post titles.

The quick-and-easy plan for adjusting the code was to comment out the archive code that I didn't want to use and replace it with a modified version of the code used to create the home page. It just needed to grab the titles and bylines (including publishing dates) and make the title a link.

There were a few other details, such as including a link at the end of the home page to archive, so the intrepid reader who scrolled all the way down could fine more posts. And that was about it for version 1.

## Making it Work for Anyone

Those tweaks would have sufficed for my site, but I felt a need to take the next step in my development as a developer: write code good enough for other people to use, not just me.

To my mind, that meant three things:

1. Make my changes a new, additional feature to the existing project, not just a tweaked version.

2. Write my feature in a way that defaults back to the standard functionality if anything goes wrong.

3. Try not to add much additional overhead to site updates.

As a bonus, I thought it would be interesting to submit a pull request and see if Mike would add my feature to his codebase.

I'm not all that self-conscious of the triviality of my changes. It adds a feature I want, it works, it doesn't remove any functionality other users might use. The first part was pretty easy. The second part added a bit of a challenge.

After thinking about the problem, it seemed like the most straightforward approach would be to add a setting. If it's set to true, my new feature gets used. A setting of false or any other value reverts to the default behavior.

    /*
        Single-page Archive
        This setting enables a single-page archive instead of
        the default day-month-year folder archives...

        A value of 'true' enables single-page archives.
        Any other value currently uses the default archive
        format.
    */
    $this->settings['singlePageArchive'] = true;

I left this as false by default as well, so anyone who pulled the code to an existing site would not be surprised by new, unexpected archive page creation. This was an important point for me: *it should not break anyone's existing site!*

From there it was a fairly straightforward task to put in my new archive creation code (adapted from Mike's original home page cration code) along with a test for the singlePageArchive setting.

That took care of my first two goals, adding new features on top of the existing ones, and not breaking the old, default features.

## Baby Steps

This is probably old hat to many programmers, but it was a pretty big step for a guy who's worked with programmers for many years, yet never written anything comprising more than 20 or 30 lines of rudimentary Python.

For starters, I'd never spent much time wading around in PHP before, and what I had done was mostly cut-and-paste coding to quickly solve a problem. The contact page on this site [_ed: deprecated in a redesign_] is a great example: someone elses's code example with a few tweaks to suit my needs.

The good news is that, over the course of many years, enough programming logic permeated my thick skull that I could follow the code, understand what it was doing, and find the interaction of functions I needed to modify — even though it was in a foreign language.

The moral of this story is that you can achieve quite a bit with a little knowledge, reference material on the web, some careful reading and persistent effort.

## What I'd Like to Do Better

There's definitely room for improvement. I have few illusions about that. So there are a few goals for the future:

Testing is something I've read much about, but haven't done properly yet. This is a high-priority area to learn and incorporate into my future projects.

My third goal was to avoid adding overhead to site operation, and that may be one area where I've failed. As implemented, any action that adds, changes or removes articles updates the entire site to make sure the archive page gets updated. A better way to handle this would be to test whether the changes actually affect the archive and only update the affected pages instead of rebuilding the site.

For a small site, this probably isn't an issue, but it would be more "right" in my mind.

Finally, I've been wanting the ability to update menus and sidebars without having to edit each page template individually — a source of several errors. So expanded templating would be nice and is on the to do list.

## Polished Is Not a Requirement

Now, while I saw putting some spit and polish on my code as a prerequisite to sharing, it's certainly not a requirement. In my case, I felt it set a reasonably high bar for my own work as well as making sure my contribution played well with someone else's existing project.

This seems to be the quality bar many others set for contributing to existing projects. Play nice. Make your changes clear. Provide passing tests. It's just good manners.

But there are plenty of cases where putting code up in public for other people to see, play with and discuss can help move an idea forward. The sentiment is pretty well summed up in this exchange between Kelly and Brandon:

<blockquote class="twitter-tweet tw-align-center" data-in-reply-to="247448093749043200"><p>@<a href="https://twitter.com/kellabyte">kellabyte</a> always. Code doesn't mature in privacy.</p>— Brandon Williams (@faltering) <a href="https://twitter.com/faltering/status/247448508964147200" data-datetime="2012-09-16T21:34:56+00:00">September 16, 2012</a></blockquote>
<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

That led to Kelly posting her initial swag at writing her own home-brew column-oriented database, [Dazzle](https://github.com/kellabyte/Dazzle), an attempt at understanding the inner workings of Cassandra by implementing her own version of it.

<blockquote class="twitter-tweet"><p>One thing I’ve learned from posting Dazzle on GitHub & code pastes in the past, embarrassed about your code only holds your progression back</p>— Kelly Sommers (@kellabyte) <a href="https://twitter.com/kellabyte/status/250981893783306240" data-datetime="2012-09-26T15:35:21+00:00">September 26, 2012</a></blockquote>
<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Success or failure, the kinds of fast, constructive feedback loops enabled by Github and similar tools are great for learning. So there's very little reason to *not* share your code.

## Interesting Times

I never doubted that public code repositories were a great idea, and the proliferation of choices — [Bitbucket](https://bitbucket.org/), Github, [Google Code](http://code.google.com/), [SourceForge](http://sourceforge.net/) and others — indicates it's a pretty popular and successful model for collaboration. And though I'd downloaded code and applications many times from these services, I never thought I'd write any code worth pushing back.

But my tiny triumph underscores how important it to just dig in and try something new. You can keep it to yourself if you want, but striving to make something you're willing to share sets the bar high, and sharing opens the door to feedback, learning and improving. Whether it's coding or writing or drawing... whatever floats your boat. Create. Share. Grow. Repeat.