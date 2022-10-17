title: Interaction of Color
date: 2017-03-25
category: art
tags: art, programming, design
summary: Josef Albers _Interaction of Color_ shows that perception of color depends greatly on the surrounding or adjacent colors. I created a web page that creates dynamically generated color swatches demonstrating one of Josef Albers' color interaction exercises.


I have recently been reading through [Josef Albers'](http://albersfoundation.org/teaching/josef-albers/introduction/) book [Interaction of Color](http://www.designersreviewofbooks.com/2010/10/interaction-of-color-by-josef-albers/) and working through some of the proposed exercies. It seemed obvious that, rather than cobbling together bits of colored paper, a web page could easily generate any number of possible color combinations.

So I built a simple page that dynamically generates the swatches described in Albers' first exercise: [Albers]({filename}/pages/albers.md)

You'll see two large fields of different colors and a small, central swatch. This central swatch is the same color within both larger fields. Notice how, depending on the surrounding colors, the central color may look different &mdash; lighter, darker, or even a slightly different shade.

Each time you refresh the page it generates a different, random selection of colors. Hex values for the generated colors are provided at the bottom of the page.

There's a fiddle if you want to play with the code: [https://jsfiddle.net/tpdorsey/wqo15gb5/](https://jsfiddle.net/tpdorsey/wqo15gb5/)

![Albers Color Swatches]({static}/images/albers.png)