title: Tap Utils for TapCellar
date: 2015-03-09
category: Programming
tags: Tech, Beer
summary: If you enjoy exploring craft beer, TapCellar is a fantastic beer journal app for iPhone. I wrote some Ruby scripts to extract interesting information from your TapCellar backups.


**Note: TapCellar is no more. Pour one out for TapCellar.**

If you enjoy exploring craft beer, [TapCellar](http://tapcellar.com/), created by my friends [Gabe](http://www.macdrifter.com/) and [Jeff](http://technologynotes.net/), is a fantastic beer journal app for iPhone. Rate the beers you've tried, share recommendations with friends, keep a shopping list, even track the contents of your beer cellar. It's a great app. Check it out.

In fact, I like TapCellar so much, I wrote [Tap Utils](https://github.com/tpdorsey/tap-utils), a collection of tiny Ruby command line scripts that let you extract interesting information from your TapCellar backup.

```text
Grade timeline for styles containing: Stout

Date        Grade F          A+  Name
2014-10-12  A               *    Imperial Russian Stout
2014-10-12  B            *       Sea Monster
2014-10-12  B+            *      Old Growth
2014-10-12  A               *    Yin
2014-10-12  B            *       Old Rasputin
2014-10-12  C         *          Overcast Espresso Stout
2014-11-11  B+            *      Milk Stout Nitro
2014-11-16  B            *       35K
2014-11-17  B+            *      Dragon's Milk
2014-11-25  A+               *   Aún Más Café Jesús
2014-12-05  A+               *   Bourbon County Brand Stout
2014-12-10  A               *    Ten Fidy

Mean Grade: A-             *
```

There are four scripts right now:

**tap-avg-grades** returns a table showing each style for which you've rated a beer, along with the average grade for the style, the number of beers rated for the style, and the standard deviation of grades. The standard deviation seemed like a clever idea at the time, but doesn't really tell you anything useful. I might change this a more relevant measurement at some point in the future.

**tap-shopping** prints out a nicely formatted ASCII shopping list from the beers in your Shopping List saved filter. You can sort the results by brewery, name, or style keywords.

**tap-styles** prints out a chart illustrating the number of graded beers for all styles with graded beers.

**tap-timeline** prints out a vertical scatter plot chart illustrating grades over time based on a name or style keyword. The screen shot above shows an example.

I learned a lot making these scripts and I hope you enjoy playing with them. There's decent documentation in the readme, and all of the utils should have ```--help``` options as well. Drink some beers, grade them in TapCellar, then print out some pretty charts. Above all else, have fun.