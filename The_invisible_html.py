#Author: Thy H. Nguyen

import webbrowser

f = open('My name is Thy.html','w')

message = """<html>


<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title> My name is Thy</title>

</head>

<body>
<p><font size="60">My </font></p>
<p><font size="60">name </font></p>
<p><font size="60">is </font></p>
<p><font size="60">Thy </font></p>



</body>


</html>


</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('My name is Thy.html')

import turtle
wn = turtle.Screen()
mom = turtle.Turtle()
mom.begin_fill()
mom.circle(50)
mom.end_fill()
mom.penup()
mom.forward(150)
mom.pendown()
mom.begin_fill()
mom.circle(50)
mom.end_fill()
mom.penup()
mom.backward(175)
mom.right(90)
mom.forward(70)
mom.pendown()
mom.begin_fill()
mom.circle(100)
mom.end_fill()
wn.exitonclick()
