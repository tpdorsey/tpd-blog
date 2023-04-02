title: VASL Mini Control Marker Extension
date: 2022-12-16
category: Games
tags: ASL
summary: A Mini Control Marker extension for VASL, an Advanced Squad Leader module for the Vassal game engine.

Mini Control Markers is an extension for VASL, an Advanced Squad Leader module for the Vassal game engine. Mini Control Markers provides markers and overlays that indicate control of a hex or location.

Current release: [mini-control-markers-0.4b.vmdx]({static}/files/mini-control-markers-0.4b.vmdx)

There are two kinds of control indicator here:

- Axis and allied control indicator overlays
- Axis and allied control indicator counters

These _do not_ replace the built-in VASL control markers, but provide additional, optional markers with a different appearance and some additional features.

Mostly, they look different: these mini control markers use smaller national icons with transparency.

The mini control overlays are a new idea. They stay in place and don’t get mixed up with counters. And they are kinda neat looking in a low key way.

![Screenshot demonstrating the use of hex control overlays.]({static}/images/overlay-preview.png)

>Credit for the idea goes to Neal Ulen and Stew Stewart. I saw Neal using something similar to this in one of his ASL Bootcamp videos and asked where he got the cool control markers. Neal's response was "The small ones are a modification done by Stew. But if you update to a new VASL version they get lost...". So I set out create my own extension version.

>Much appreciation to Neal for his time testing and giving feedback on early versions of this extension.

Between the axis and allied versions, they currently support the following individual nation icons:

Allied: Russia (PRoC, DPRK), US, Britain, France, Free French, Poland, Nationalist China (RoC), RoK.

Axis: Germany, Finland, Italy, France, Japan, RoC.

![Screenshot demonstrating use of location control counters.]({static}/images/overlay-icons.png)

The counters are for folks who want the traditional control counter experience, but with transparent counters. The counters are stackable for control that is specific to, for example, building levels.

![Screenshot demonstrating location control counters in a counter stack.]({static}/images/counter-stack.png)

The control counters also show up correctly for the hover popover for a hex.

![Screenshot demonstrating location control counters in the VASL counter preview.]({static}/images/counter-preview.png)

Both the mini markers and mini overlays support Ctrl-F "Flip" to switch between axis and allied markers/overlays. When you flip, it logs a control change message with the affected hex to the chat.

You'll find the overlays in **Draggable Overlays > Map Annotations > Mini Control Indicators**. There's an Allied mini control overlay and an Axis mini control overlay.

![Screenshot showing the location of control overlays in VASL.]({static}/images/overlays.png)

They support the following commands:

- Shift-select      - Select overlay
- Ctrl-[ and Ctrl-] - Toggle nation icons
- Ctrl-F            - “Flip” between Axis and Allied control

You'll find the counters in **VASL Counters > Other > Map > Mini Control Markers**. There's an Allied control counter with transparency and Axis control counter with transparency.

![Screenshot showing the location of control counters in VASL.]({static}/images/counters.png)

They support the same commands as the default VASL control counters, including:

- Ctrl-[ and Ctrl-] - Toggle nation icons
- Ctrl-F            - “Flip” between Axis and Allied control