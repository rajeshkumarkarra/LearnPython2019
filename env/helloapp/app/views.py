from django.shortcuts import render

# Create your views here.
import textwrap

from django.http import HttpResponse
from django.views.generic.base import View

class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <!DOCTYPE html>
<html>
<head>
	<!-- <title> is used to display the actual page title on web browser-->
	<title>My First HTML</title>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>html</title>
	<link rel="stylesheet" href="">
	
</head>
	<link rel="stylesheet" href="/html/styles.css">
	
	

<!--
	background-color for background color
	font-size for sizing the font
	color is for coloring the font
	font-family is for font style
	text-align for alignment of text(right-centre-left)

	Formatting elements were designed to display special types of text:

	<b> - Bold text
	<strong> - Important text
	<i> - Italic text
	<em> - Emphasized text
	<mark> - Marked text
	<small> - Small text
	<del> - Deleted text
	<ins> - Inserted text
	<sub> - Subscript text
	<sup> - Superscript text
-->


<body style="background-color: rgba(255, 99, 71,  0.2);">
	<!-- <h1> is for heading and STYLE is an attribute for font size-->
	<h1 style="font-size:70px; color:red; font-family:verdana; text-align:center;background-color:mediumseagreen" ><q>Domus Dux</q></h1>
	<!-- p is for paragraph and style is an attribute for color here, and here an attribute
		of TITLE is used to display the actual title name when place the cursor on the paragraph
		and <br> is used to break the content-->
	<hr>
	<p style="color:stayblue; font-family:courier; text-align:right;background-color: gray" title="I'm a tooltip "><b>Name:</b> <mark>Rajesh K. Kumar</mark> <br><b>Mobile:</b> 8886814149<br> <b>Email:</b> <q>
	<a href="rajeshkumarkarra.github.io">rajeshkumarkarra.github.io</a></q><br><b><cite>My Address</cite>:</b> <small>Hyderabad</small>, IND</p>
	<!--
	<address>
		Hyderabad,<br>
		IND.
	</address>
	-->
		<!-- here tag <hr>(horizontal) is used to seperate the content horizontally
	<p style="color:green; text-align:right; font-family:courier"><b>My Address:</b> <i><small>Hyderabad</small></i></p>

	-->
	<hr>
	<!-- HTML links are defined with the <a> tag. The link address is specified in the href attribute:-->
	<a href="rajeshkumarkarra.github.io"><em>email me</em></a>
	<!-- img for image, src is used to image source, 
		The alt attribute specifies an alternative text to be used, when an image cannot be displayed.-->
	<img src="file:///home/rajesh/Downloads/main-qimg-611ed3c77d17db7551e3a6c568cfe481.webp" alt="w3school.com" width="104" height="104">
	<button type="">Click Me</button>
	<!-- <ul> means unordered list
		<ol> means ordered list
			<li> means list-->
	<ul>
		<li>desserts</li>
		<li>cookies</li>
		<li><del>scimmed milk  </del><ins>Milk</ins> </li>
		<li>Bru</li>
	</ul>
	<ol>
		<li><sup>Coffee</sup></li>
		<li><sub>Tea</sub></li>
		<li>Milk</li>
	</ol>

<p>
  My Bonnie lies over the ocean.

  My Bonnie lies over the sea.
  
  My Bonnie lies over the ocean.

  Oh, bring back my Bonnie to me.
</p>
<!-- <pre> stands for pre-formatted text used to show the content as given by the user-->
<pre>
  My Bonnie lies over the ocean.

  My Bonnie lies over the sea.

  My Bonnie lies over the ocean.

  Oh, bring back my Bonnie to me.
</pre>
	
</body>
</html>
        ''')
        return HttpResponse(response_text)