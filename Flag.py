import turtle
from math import sqrt

wn = turtle.Screen()                      #Screen
wn.bgcolor("lightblue")                   #Background colour (lightblue)
wn.title("Program that draws flags")      #Screen's name
f = turtle.Turtle()                       #Turtle's name
f.speed(17)                                #Turtle's speed

#---Variables---

l = 80    #Flag's width
L = 40    #Flag's length

#=====FUNCTIONS=====

#---Vertical Flag---

def vertical_flag(c1,c2,c3):
    """pre: color1, color2, color3 must be a string (ex: "red","green","blue",...)
            Put the colors starting from the left.
       post: Draws a vertical flag with the wanted colors.
    """
    for z in [c1,c2,c3]:
        f.pencolor(z)
        f.fillcolor(z)
        f.begin_fill()

        f.left(90)
        f.fd(l)
        f.right(90)
        f.fd(L)
        f.right(90)
        f.fd(l)
        f.right(90)
        f.fd(L)
        f.right(180)
        f.fd(L)
        f.end_fill()


#---SPACE---
def space(sp):
    """pre: The turtle must be in the right bottom of the flag
            and must point forward
       post: Makes a space between the drawings
    """
    f.up()
    f.forward(sp)
    f.down()
    
#---Horizontal Flag---

def horiz_flag(c1, c2, c3):
    """pre: color1, color2, color3 must be a string (ex: "red","green","blue",...)
            Put the colors starting from the bottom.
       post: Draws a 3 horizontal's strip flag with the wanted colors.
    """
    for k in [c1,c2,c3]:
        f.pencolor(k)
        f.fillcolor(k)
        f.begin_fill()
        
        f.fd(3*L)
        f.left(90)
        f.fd(l/3)
        f.left(90)
        f.fd(3*L)
        f.left(90)
        f.fd(l/3)
        f.right(180)
        f.up()
        f.fd(l/3)
        f.right(90)
        f.down()
        f.end_fill()
        
    f.up()
    f.fd(L*3)
    f.right(90)
    f.fd(l)
    f.left(90)

#---Star Function---

def star(lt,color):
    """pre: lt>0 and color must be a string (ex: "red","green","blue",...)
       post: Draws a 5 branch star with the lenght and the color wanted
    """
    f.pencolor(color)
    f.fillcolor(color)
    f.begin_fill()
    for k in range(5):
        f.right(144)
        f.fd(lt)
    f.end_fill()

#---2 horizontal's strip flag---

def horiz_flag_2b(c1,c2):
    """pre: color1, color2 must be a string (ex: "red","green","blue",...)
            Put the colors starting from the bottom
       post: Draws a 2 horizontal's strip flag with the wanted color
    """
    f.pencolor(c1)
    f.fillcolor(c1)
    f.begin_fill()
    for j in range(1,3):
        f.fd(3*L)
        f.left(90)
        f.fd(l/2)
        f.left(90*j)
    f.fd(l/2)
    f.end_fill()

    f.pencolor(c2)
    f.fillcolor(c2)
    f.begin_fill()
    for i in range(2):
        f.right(90*i)
        f.fd(l/2)
        f.right(90)
        f.fd(L*3)
    f.end_fill()
    f.up()
    f.left(90)
    f.fd(l/2)
    f.left(90)
    f.fd(3*L)
    f.down()

#---Line break Function---

def line_break(flag_nbr):
    """pre: nbr must be an int/float
       post: Makes a line break
    """
    f.up()
    f.backward((3*L)*(flag_nbr)+5*30)
    f.right(90)
    f.fd(110)
    f.left(90)
    f.down()


#=======================================================

alinea = -450      #The gap between de left side of the screen and the drawing's start

f.up()
f.left(180)
f.backward(alinea)
f.right(90)
f.fd(-(alinea/5))
f.right(90)
f.down()
vertical_flag("black","gold","red")           #Vertical flag 1
space(30)
vertical_flag("blue","white","red")           #Vertical flag 2
space(30)

#=========================================================

#---Israelian flag---

f.pencolor("mediumblue")
f.fillcolor("mediumblue")
f.begin_fill()
f.forward(3*40)
f.left(90)
f.forward(10)
f.left(90)
f.forward(3*40)
f.left(90)
f.forward(10)
f.left(180)
f.end_fill()

f.pencolor("white")
f.fillcolor("white")
f.begin_fill()
f.up()
f.fd(10)
f.down()
f.forward(60)
f.right(90)
f.fd(3*40)
f.right(90)
f.fd(60)
f.right(90)
f.fd(40*3)
f.right(90)
f.end_fill()

f.up()
f.fd(60)
f.down()

f.pencolor("mediumblue")
f.fillcolor("mediumblue")
f.begin_fill()
f.fd(10)
f.right(90)
f.fd(3*40)
f.right(90)
f.fd(10)
f.right(90)
f.fd(40*3)
f.end_fill()

#The jewish star
c = 45            #One side lenght
epaisseur = 2.75  #Of the star

f.pensize(epaisseur)
f.pencolor("mediumblue")
f.right(180)
f.up()
f.fd(60)
f.right(90)
f.fd(8)
f.right(30)
f.down()
f.fd(c)
f.left(120)
f.fd(c)
f.left(120)
f.fd(c)

f.left(150)
f.up()
f.fd(50)
f.down()
f.right(180)
f.right(30)
f.fd(c)
f.left(120)
f.fd(c)
f.left(120)
f.fd(c)

f.right(30)
f.up()
f.fd(12)
f.left(90)
f.fd(60)
f.down()
f.pensize(1)

#---3 more flags---
space(30)
vertical_flag("green", "white", "red")         #Vertical flag 3
space(30)
horiz_flag("gold", "red", "black")             #Horizontal flag 1
space(30)
horiz_flag("red", "mediumblue", "white")

#---Line break---
line_break(6)
# f.backward((3*L)*6+5*30)
# f.right(90)
# f.fd(110)
# f.left(90)
# f.down()
#---2 more flags---
vertical_flag("darkblue","yellow","red")
space(30)
horiz_flag("steelblue3","white","red")
space(30)

#---Catalan Flag---

for i in range(4):
    
    f.pencolor("yellow")               #yellow line
    f.fillcolor("yellow")
    f.begin_fill()
    f.left(90)
    f.fd(l/9)
    f.right(90)
    f.fd(3*L)
    f.right(90)
    f.fd(l/9)
    f.right(90)
    f.fd(3*L)
    f.right(90)
    f.fd(l/9)
    f.end_fill()

    f.pencolor("red")                    #red line
    f.fillcolor("red")
    f.begin_fill()
    f.fd(l/9)
    f.right(90)
    f.fd(3*L)
    f.right(90)
    f.fd(l/9)
    f.right(90)
    f.fd(3*L)
    f.right(90)
    f.fd(l/9)
    f.right(90)
    f.end_fill()

f.pencolor("yellow")       #preparing the turtle's position
f.fillcolor("yellow")
f.begin_fill()
f.left(90)
f.fd(l/9)
for i in range(2):        #the last yellow line at the top
    
    f.right(90)
    f.fd(3*L)
    f.right(90)
    f.fd(l/9)
f.right(90)
f.end_fill()

f.pencolor("darkblue")            #blue triangle on the left
f.fillcolor("darkblue")
f.begin_fill()
f.right(45)
f.fd(sqrt((80**2/4)+(40**2)))
f.right(90)
f.fd(sqrt((80**2/4)+(40**2)))
f.right(-45)
f.end_fill()

f.right(180)              #Center the star in the triangle
f.fd((l/2)+3)
f.right(90)
f.fd(L/2)

star(15,"white")    #The Catalan star
#-----------------

f.up()            #go back to the end of the flag(at the bottom right)
f.fd((L/2)+2*L)
f.right(90)
f.fd(l/2)
f.left(90)
f.down()

#---2 more flags---

space(30)
horiz_flag("red","darkgreen","white")
space(30)
horiz_flag_2b("red","white")
space(30)

#---Greek Flag---

for i in range(4):
    f.pencolor("royalblue")               #royalblue line
    f.fillcolor("royalblue")
    f.begin_fill()
    f.left(90)
    f.fd(l/9)
    f.right(90)
    f.fd(3*L)
    f.right(90)
    f.fd(l/9)
    f.right(90)
    f.fd(3*L)
    f.right(90)
    f.fd(l/9)
    f.end_fill()

    f.pencolor("white")                    #white line
    f.fillcolor("white")
    f.begin_fill()
    f.fd(l/9)
    f.right(90)
    f.fd(3*L)
    f.right(90)
    f.fd(l/9)
    f.right(90)
    f.fd(3*L)
    f.right(90)
    f.fd(l/9)
    f.right(90)
    f.end_fill()

f.pencolor("royalblue")       #preparing the turtle's position
f.fillcolor("royalblue")
f.begin_fill()
f.left(90)
f.fd(l/9)
for i in range(2):        #the last royalblue line at the top
    f.right(90)
    f.fd(3*L)
    f.right(90)
    f.fd(l/9)
f.right(90)

f.fd(L)             #Square on the left side
f.right(90)
f.fd(5*(l/9))
f.right(90)
f.fd(L)
f.right(90)
f.fd(5*(l/9))
f.right(90)
f.end_fill()
    

f.fd(L/2-((l/9)/2))        #preparing the turtle's position
f.right(180)

for i in range(2):          #suare's vertical line 
    f.pencolor("white")               
    f.fillcolor("white")
    f.begin_fill()
    f.left(90)
    f.fd(5*(l/9))
    f.left(90)
    f.fd(l/9)
    f.end_fill()

f.up()                      #preparing turtle's position
f.fd(L/2-((l/9)/2))
f.left(90)
f.fd(2*l/9)
f.down()

f.pencolor("white")            #square's horizontal line   
f.fillcolor("white")
f.begin_fill()
f.left(90)
for j in range(2):
    f.right(90*j)
    f.fd(L)
    f.right(90)
    f.fd(l/9)
f.end_fill()

f.up()           #Goes to the bottom right of the flag
f.fd(2*l/9)
f.right(90)
f.fd(3*L)
f.right(90)
f.fd(l)
f.left(90)
f.down()
#------------
f.up()
line_break(6)
#---Rep tch Flag---
horiz_flag_2b("red","white")
f.ht()
f.up()                        #Goes to the top left
f.left(90)
f.fd(l)
f.left(90)
f.fd(3*L)
f.right(180)
f.st()

f.pencolor("blue4")            #blue triangle on the left
f.fillcolor("blue4")
f.begin_fill()
f.right(45)
f.fd(sqrt((80**2/4)+(40**2)))
f.right(90)
f.fd(sqrt((80**2/4)+(40**2)))
f.right(-45)
f.end_fill()
f.up()
f.left(90)
f.fd(3*L)
f.down()
#--------------------
space(30)
#---Vietnam flag---
f.pencolor("red")          #red background
f.fillcolor("red")
f.begin_fill()
f.left(90)
f.fd(l)
f.right(90)
f.fd(3*L)
f.right(90)
f.fd(l)
f.right(90)
f.fd(3*L)
f.end_fill()

f.up()      #centring the star
f.right(90)
f.fd((l/2)+5)
f.right(90)
f.fd((2*L)+5)
star(50, "yellow")    #Draws the star

f.up()          #Goes to the bottom right
f.right(90)
f.fd((l/2)+5)
f.left(90)
f.fd((3*L)-((2*L)+5))
#----------------------
space(30)

#---Japan flag---

f.pencolor("white")          #white background
f.fillcolor("white")
f.begin_fill()
f.left(90)
f.fd(l)
f.right(90)
f.fd(3*L)
f.right(90)
f.fd(l)
f.right(90)
f.fd(3*L)
f.end_fill()

f.right(90)     #Goes to flag's center
f.fd(l/(5))
f.right(90)
f.fd((3*L)/2)

f.pencolor("firebrick")    #Draws the circle in the middle
f.fillcolor("firebrick")
f.begin_fill()
f.circle(L/1.75)
f.end_fill()

f.up()               #Goes back to the bottom right
f.right(90)
f.fd(l/5)
f.left(90)
f.fd((3*L)/2)
f.down()
#-----------------
space(30)
#---Quatar Flag---

vertical_flag("darkmagenta","darkmagenta","darkmagenta")  #Magenta background

f.right(180)          #Left side (rectangle)
f.fd(2*L+2*L/3)
f.pencolor("white")    
f.fillcolor("white")
f.begin_fill()
f.fd(L/3)
f.right(90)
f.fd(l)
f.right(90)
f.fd(L/3)
f.right(90)
f.fd(l)
f.end_fill()

f.left(90)    #Orientation of the turtle
f.left(45)

for u in range(5):       #The triangles on the left
    f.pencolor("white")
    f.fillcolor("white")
    f.begin_fill()
    f.fd(l/7)
    f.left(90)
    f.fd(l/7)
    f.right(90)
    f.end_fill()
    
f.right(45)     #Goes to the bottom right
f.up()
f.fd(2*L+2*L/3)
f.right(90)
f.fd(l)
f.left(90)
f.down()
#---2 more flags---
space(30)
horiz_flag("white","black","darkblue")
space(30)
vertical_flag("limegreen","gold","firebrick")
f.down()                     #In case..., precaution :)
line_break(6)

#---Swedish Flag---

f.pencolor("dodgerblue4")    #DodgerBlue background
f.fillcolor("dodgerblue4")
f.begin_fill()
for i in range(2):
    f.left(90*i)
    f.fd(3*L)
    f.left(90)
    f.fd(l)
f.left(90)
f.end_fill()

f.fd(L)           #Preparing the turtle's position
f.left(90)

f.pencolor("yellow")    #Vertical yellow band 
f.fillcolor("yellow")
f.begin_fill()
for j in range(2):
    f.right(90*j)
    f.fd(l)
    f.right(90)
    f.fd(10)
f.end_fill()

f.up()                 #Preparing the turtle's position
f.fd(L)
f.right(90)
f.fd((l/2)+5)
f.right(90)
f.down()

f.pencolor("yellow")             #Horizontal yellow band
f.fillcolor("yellow")
f.begin_fill()
for z in range(0,2):
    f.right(90*z)
    f.fd(3*L)
    f.right(90)
    f.fd(10)
f.end_fill()

f.up()            #Goes to the bottom right
f.right(180)
f.fd((l/2)+5)
f.left(90)
f.fd(3*L)
#---------------
space(30)
horiz_flag_2b("yellow","skyblue3")

#----English Flag-----------
space(30) 
f.pencolor("white")      #White rectangle          
f.fillcolor("white")
f.begin_fill()
f.fd(3*L)
f.left(90)
f.fd(2*L)
f.left(90)
f.fd(3*L)
f.left(90)
f.end_fill()

f.up()                   #Vertical red strip
f.pencolor("red")
f.fillcolor("red")
f.begin_fill()
f.left(90)
f.fd(50)
f.right(90)
f.down()
f.fd(l)
f.left(90)
f.fd(20)
f.left(90)
f.fd(l)
f.left(90)
f.fd(20)
f.end_fill()

f.up()    #Preparing the turtle's position for the upcoming horizontal red band
f.fd(50)
f.left(90)
f.fd(30)
f.down()

f.fillcolor("red")   #Horizontal red strip
f.begin_fill()
f.left(90)
f.fd(3*L)
f.right(90)
f.fd(20)
f.right(90)
f.fd(3*L)
f.right(90)
f.fd(20)
f.end_fill()

f.up()          #Goes to the bottom right
f.fd(30)
f.right(90)
f.fd(3*L)
f.right(90)
f.fd(l)
f.left(90)
#---------------

#---------------
# 
# f.pencolor("red")             #Horizontal yellow band
# f.fillcolor("red")
# f.begin_fill()
# f.left(90)
# f.fd(l)
# f.right(90)
# f.fd((3*L)-20)
# f.right(90)
# f.fd(l)
# f.right(90)
# f.fd((3*L)-20)
# f.end_fill()
# 
# f.right(90)
# f.fd((l/2)+5)
# f.right(90)
# f.fd(20)
# 
# f.pencolor("white")             #Horizontal yellow band
# f.fillcolor("white")
# f.begin_fill()
# for x in range(0,2):
#     f.right(90*x)
#     f.fd((3*L)-60)
#     f.right(90)
#     f.fd(10)
# f.end_fill()
# 
# f.up()
# f.right(90)
# f.backward(20)
# f.right(90)
# f.fd((l/2)+5)
# f.left(90)
# f.fd((((3*L)-20)/2))
# f.backward(5)
# f.left(90)
# f.fd(15)
# f.down()
# # f.fd((((3*L)/2)-10)/2)
# 
# 
# 
# f.pencolor("white")             #Horizontal yellow band
# f.fillcolor("white")
# f.begin_fill()
# for y in range(0,2):
#     f.right(90*y)
#     f.fd(((l/2)+20))
#     f.right(90)
#     f.fd(10)
# f.end_fill()

#---------------