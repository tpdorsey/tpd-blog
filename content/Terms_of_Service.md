title: Terms of Service
date: 2013-01-03
category: Opinion
tags: Tech, Business
summary: Online services are going to steal all of our content and use it to enrich themselves. Or maybe they're not. Some thoughts on copyright, online services, and TOS language.


**Updated below on 1/3 and 1/16**

**Note: this is an old piece, some of the linked documents may no longer contain the referenced terms. Some may no longer exist at all.**

Online services are going to steal all of our content and use it to enrich themselves. Or maybe they're not. It makes for great paranoid headlines whenever a popular site updates their terms of services, but what's really happening here?

[IANAL](http://en.wikipedia.org/wiki/IANAL) and have no particular expertise in the areas of [IP law](http://www.aipla.org/about/iplaw/Pages/default.aspx), so you'd be wise to rely on your own judgement and the advice of an attorney rather than my insight. However, I think there's a lot we can learn from a close reading of actual terms of service and a little common sense.

I was inspired to write about this by a tweet from [Hal Berenson](https://twitter.com/halberenson/status/285752757175087108), linking to a post by [Bruce Schneier](http://www.schneier.com/blog/archives/2012/12/terms_of_servic.html), suggesting that, if you "Store something in the cloud... the cloud service owns it."

Schneier mentions the recent dust-up about [Instagram's terms of service](http://allthingsd.com/20121224/happy-holidays-instagram-here-have-a-class-action-lawsuit/), and if you've been paying attention, you also know that [Twitter](http://arstechnica.com/tech-policy/2008/05/twitters-controversy-over-terms-of-service/), [Facebook](http://consumerist.com/2009/02/15/facebooks-new-terms-of-service-we-can-do-anything-we-want-with-your-content-forever/) and other services have faced similar controversy over their TOS language.

The general uproar is something along the lines of:

"OMG ALL YOUR CONTENT ARE BELONG TO [service du jour] AND THEY CAN DO ANYTHING THEY WANT WITH IT!"

What's this all about? Why is [service du jour] suddenly stealing everyone's photos, wry observations, presentations or whatever? And what are they going to do with all this booty?

## All Rights Reserved

The problem rests in some fundamental misunderstandings about how we use copyrighted works.

When you create something — write a tweet or a blog post, take a photo, sing a song and so on — the copyright for it is granted automatically (and in most cases, to you... though there are exceptions). If someone else wants to use it, they need your permission: you can grant a *license* for them to use that writing or photo or song under certain conditions.

And that's exactly what's happening here. You take a photo. You have a copyright on that photo. You upload it to Instagram. For them to do *anything* with that photo, you need to give Instagram permission — a license — to reproduce your copyrighted content and save a copy on their server.

Say you want Instagram to let your friends see the photo. You're smart and know how computers work; think about the further consequences: Instagram has to make and distribute copies of your photo for each person who wants to see it. Maybe they distribute files around to servers for load balancing or CDN-style distribution. More copies. Hopefully they back up your data. More copies.

They need your explicit permission to copy and distribute your copyrighted work.

Of course, lawyers being lawyers, and corporations being corporations, they use very-broad-and-yet-very-specific language to cover their asses in all the ways they can possibly think of, plus a few ways both you and they haven't imagined yet.

So you end up with terms of service language that sounds like OMG ALL MY FILES BELONG TO...

## Licentious Behavior

Take a deep breath. Maybe it's not that bad after all.

In a previous life, part of my job involved proofreading [EULA](http://en.wikipedia.org/wiki/End-user_license_agreement) text for software installers. Yes, it was dull. But, the benefits! If you'd ever read through *all* of a EULA, a rental or mortgage contract or any similar legal document, you'd know that most of the language looks remarkably similar from one contract to another... it's boilerplate. Why reinvent the wheel? If it works in one situation (and holds up in court), use it again and again and....

Going back to that Bruce Schneier post, the objection focused on this particular text in the [Prezi Terms of Use](http://prezi.com/terms-of-use/#toc4), Prezi being a service that lets you upload and share presentations or something to that effect. Specifically, there were concerns about the section dealing with User Content & Options:

>In order to provide you with the Service, it is necessary for you to grant Prezi certain licenses to your User Content.

>With respect to Public User Content, you hereby do and shall grant to Prezi (and its successors, assigns, and third party service providers) **a worldwide, non-exclusive, perpetual, irrevocable, royalty-free, fully paid, sublicensable, and transferable license to use, reproduce, modify, create derivative works from, distribute, publicly display, publicly perform, and otherwise exploit the content**...

(My emphasis here and throughout, by the way, unless otherwise stated.)

That sounds pretty sinister. Promising to "exploit" is rarely a great way to make friends. In addition, Prezi requires you to grant a similar license to anyone who views your public content:

>When you upload User Content on or through the Service, you also hereby do and shall grant to each user of the Service with whom you share your presentation a personal non-commercial non-exclusive license to access and view your User Content.

Yikes! What are they doing with my presentation?

But hang on. Think back to what I metioned earlier. They need your *explicit permission* to make any copies of your content that live on their servers or move around their service, any copies displayed to other users of the service and any copies needed for features of their service they haven't implemented or even thought up yet. That is what your "worldwide, non-exclusive, perpetual, irrevocable, royalty-free, fully paid, sublicensable, and transferable license" enables Prezi to do without fear of being sued for copyright infringement.

## Boilerplate Special

I mentioned [my interpretation of the license terms](https://twitter.com/tpdorsey/status/285769968564441089) to Hal, who replied that ["Microsoft has no rights other than those necessary to operate [the] service"](https://twitter.com/halberenson/status/285798135299719168), offering Microsoft's terms of service as a counterexample to Prezi's.

It's a fair point to the extent that [Microsoft Services Agreement](http://windows.microsoft.com/en-US/windows-live/microsoft-services-agreement) section 3.1 does explicitly state "[W]e do not claim ownership of the content you provide on the services. Your content remains your content...."

I believe that to be entirely true and put in fairly straightforward terms. Further, they make the entirely valid point that other people may see, save and reproduce copies:

>If you share content in public areas of the services or in shared areas available to others you’ve chosen, you agree that anyone you have shared content with may, for free, use, save, reproduce, distribute, display, and transmit that content in connection with their use of the services and other Microsoft, or its licensees’, products and services. **If you don't want others to have that ability, don't use the services to share your content.**

Well said.

However, if we read a bit further, we'll see something a bit more like that Prezi license language start to show up:

>When you upload your content to the services, **you agree that it may be used, modified, adapted, saved, reproduced, distributed, and displayed to the extent necessary** to protect you and to provide, protect and improve Microsoft products and services.

Sounds simple enough. But wait, these are not the only terms you're agreeing to. For example, head over to SkyDrive. The terms of service are a little more difficult to find, but eventually you'll end up at the [Terms of Use](http://www.microsoft.com/About/Legal/EN/US/IntellectualProperty/Copyright/default.aspx) page. Again, it includes the benign-looking prelude "Microsoft does not claim ownership of the materials you provide to Microsoft," but there's more:

>...you are granting Microsoft, its affiliated companies and necessary sublicensees permission to use your Submission... **including, without limitation, the license rights to: copy, distribute, transmit, publicly display, publicly perform, reproduce, edit, translate and reformat** your Submission... **and the right to sublicense such rights to any supplier of the Services.**

Looks familiar?

## It's Non-Exclusive

For better or worse, you're going to see language like this being used by pretty much any significant player in online or cloud services.

Here's [Twitter's version](https://twitter.com/tos), under the section helpfully titled "Your Rights":

>You retain your rights to any Content you submit, post or display on or through the Services. By submitting, posting or displaying Content on or through the Services, you grant us **a worldwide, non-exclusive, royalty-free license (with the right to sublicense) to use, copy, reproduce, process, adapt, modify, publish, transmit, display and distribute** such Content in any and all media or distribution methods (now known or later developed).

As the tip on the page notes, "This license is you authorizing us to make your Tweets available to the rest of the world and to let others do the same."

Let's take a look at Facebook's [Statement of Rights and Responsibilities](https://www.facebook.com/legal/terms), under "Sharing Your Content and Information":

>You own all of the content and information you post on Facebook, and you can control how it is shared through your privacy and application settings. In addition... you grant us **a non-exclusive, transferable, sub-licensable, royalty-free, worldwide license** to use any IP content that you post on or in connection with Facebook (IP License).

Or maybe you should check out the "Your Content in our Services" section of [Google's Terms of Service](http://www.google.com/intl/en/policies/terms/):

>Some of our Services allow you to submit content. You retain ownership of any intellectual property rights that you hold in that content. In short, what belongs to you stays yours.

>When you upload or otherwise submit content to our Services, you give Google (and those we work with) **a worldwide license to use, host, store, reproduce, modify, create derivative works...communicate, publish, publicly perform, publicly display and distribute such content**. The rights you grant in this license are for the limited purpose of operating, promoting, and improving our Services, and to develop new ones.

It's a little harder to find (conspiracy theory anyone?), but Apple's [iCloud Terms And Conditions](http://www.apple.com/legal/icloud/en/terms.html) aren't much different:

>Apple does not claim ownership of the materials and/or Content you submit or make available on the Service. However, by submitting or posting such Content on areas of the Service... you grant Apple **a worldwide, royalty-free, non-exclusive license to use, distribute, reproduce, modify, adapt, publish, translate, publicly perform and publicly display** such Content on the Service...

Birds do it, bees do it. Everybody on the web seems to do it. Let's do it. Let's accept that these license terms are basically industry boilerplate and move on.

## Fox In The Hen House

Just to be clear, I'm not trying to belittle the comments made by Hal or Bruce... or anyone else who has concerns about this widely used, easily misunderstood — and perhaps easily abused? — licensing language.

I believe it is essentially boilerplate and meant to cover legitimate business use of our photos, videos, jokes and memories. Thus far, I can't think of any businesses that have, in fact, appropriated user content for reasons not intended by the user. And given the backlash resulting just from the *suggestion* that it might happen, I can't see why any sanely run business would try to do so.

But the ideas that are unacceptable today may become more acceptable tomorrow. Perhaps a future startup tries explicitly employing user content as part of its service, creating a wedge that makes the practice tempting where it was previously taboo. Of course, people tend to do stupid things, so maybe it's just a matter of time for someone to exploit this broad licensing language, consequences be damned.

In the meantime, the bold headlines seem more click-bait than Cassandra.

**Update:** Well, well, well... [Ryan Singel points out](https://twitter.com/rsingel/status/287317832197349376) that BuzzFeed is already raising significant investment funding on a "biz model of willful copyright infringement." Sure, they're taking liberties with photos folks have posted to other services — you haven't licensed them anything — but is this the "wedge that makes the practice tempting where it was previously taboo," or an outlaw site, doomed to failure?

My point stands, however: these terms of service aren't the problem (yet). Bad actors are.

**Update 2:** Today Reuters reports that [News outlets improperly used photos posted to Twitter](http://www.reuters.com/article/2013/01/15/us-socialmedia-copyright-ruling-idUSBRE90E11P20130115). According to the story, a reporte at Agence France-Presse took photos that photographer Daniel Morel had posted on Twitter, used them in an AFP story without permission, then passed them on to Getty Images, from whom the Washington Post procured the images.

>AFP had argued that Twitter's terms of service granted it the right to use Morel's images.

>The judge, though, said that while the service terms do allow the reposting and rebroadcasting of users' images in certain circumstances, such as "retweeting" them, it does not grant a license for commercial use....

>Twitter was not a party in the case. "As has always been our policy, Twitter users own their photos," a Twitter spokesman said.

As before, I think this is a case of misappropriation &mdash; and a journalist at an organization of this stature should really know better.