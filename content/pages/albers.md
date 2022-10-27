title: Albers


Josef Albers' _Interaction of Color_ shows that perception of color depends greatly on the surrounding or adjacent colors. This page creates dynamically generated color swatches demonstrating one of Josef Albers' color interaction exercises: how the appearance of one color may vary to the observer based on another color immediately surrounding the first color.

Each time you refresh the page it generates a different, random selection of colors. Note that the central color may look slightly lighter or darker between the two examples, but it's always the exact same color!

Hex values for the generated colors are provided at the bottom of the page.

<style media="screen" type="text/css">

/* body {background: white;} */

#container1 {
    background: silver;
    width: 100px;
    height: 100px;
    margin: 10px auto;
    border: 250px solid;
    border-color: lightgray;}

#container2 {
    background: silver;
    width: 100px;
    height: 100px;
    margin: 10px auto;
    border: 250px solid;
    border-color: darkgray;}

#colordata {
    font-family: sans-serif;
    color: lightgray;
    width: 600px;
    margin-left: auto;
    margin-right: auto;
    padding-top: 20px;
}
</style>

</head>
<body>

<div id="container1">
    <p></p>
</div>

<div id="container2">
    <p></p>
</div>

<div id="colordata"></div>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<script>
  get_random = function (list) {
    return list[Math.floor((Math.random()*list.length))];
  }

  get_three_colors = function(list) {
    var clrs = [];

    while (clrs.length < 4) {
      var temp_color = get_random(list);

      if (!(clrs.includes(temp_color))) {
        clrs.push(temp_color);
      }
    }

    return clrs;
  }

  function rgb2hex(rgb){
    rgb = rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
    return "#" +
      ("0" + parseInt(rgb[1],10).toString(16)).slice(-2) +
      ("0" + parseInt(rgb[2],10).toString(16)).slice(-2) +
      ("0" + parseInt(rgb[3],10).toString(16)).slice(-2);
  }

  var colors = ["black","silver","gray","white","maroon","red","purple","fuchsia","green","lime","olive","yellow","navy","blue","teal","aqua","orange","aliceblue","antiquewhite","aquamarine","azure","beige","bisque","blanchedalmond","blueviolet","brown","burlywood","cadetblue","chartreuse","chocolate","coral","cornflowerblue","cornsilk","crimson","cyan","darkblue","darkcyan","darkgoldenrod","darkgray","darkgreen","darkgrey","darkkhaki","darkmagenta","darkolivegreen","darkorange","darkorchid","darkred","darksalmon","darkseagreen","darkslateblue","darkslategray","darkslategrey","darkturquoise","darkviolet","deeppink","deepskyblue","dimgray","dimgrey","dodgerblue","firebrick","floralwhite","forestgreen","gainsboro","ghostwhite","gold","goldenrod","greenyellow","grey","honeydew","hotpink","indianred","indigo","ivory","khaki","lavender","lavenderblush","lawngreen","lemonchiffon","lightblue","lightcoral","lightcyan","lightgoldenrodyellow","lightgray","lightgreen","lightgrey","lightpink","lightsalmon","lightseagreen","lightskyblue","lightslategray","lightslategrey","lightsteelblue","lightyellow","limegreen","linen","mediumaquamarine","mediumblue","mediumorchid","mediumpurple","mediumseagreen","mediumslateblue","mediumspringgreen","mediumturquoise","mediumvioletred","midnightblue","mintcream","mistyrose","moccasin","navajowhite","oldlace","olivedrab","orangered","orchid","palegoldenrod","palegreen","paleturquoise","palevioletred","papayawhip","peachpuff","peru","pink","plum","powderblue","rosybrown","royalblue","saddlebrown","salmon","sandybrown","seagreen","seashell","sienna","skyblue","slateblue","slategray","slategrey","snow","springgreen","steelblue","tan","thistle","tomato","turquoise","violet","wheat","whitesmoke","yellowgreen","rebeccapurple"];

  var color_list = get_three_colors(colors);

  var center = color_list[0];
  var field1 = color_list[1];
  var field2 = color_list[2];

  $(function() {
    $('#container1').css('background', center);
    $('#container1').css('border-color', field1);
    $('#container2').css('background', center);
    $('#container2').css('border-color', field2);
    var centercolor = $( '#container1' ).css( "background-color" );
    var topcolor = $( '#container1' ).css( "border-color" );
    var bottomcolor = $( '#container2' ).css( "border-color" );
    $( "#colordata" ).html(
      "Center color: " + center + " (" + rgb2hex(centercolor) + ")<br>" +
      "Top Color: " + field1 + " (" + rgb2hex(topcolor) + ")<br>" +
      "Bottom Color: " + field2 + " (" + rgb2hex(bottomcolor) + ")" );
  });
</script>