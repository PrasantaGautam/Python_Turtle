
from turtle import *
import turtle


# screensize(1000,1000)

##
bgcolor("black")
color("black")

##
color("blue")
fillcolor("red")
begin_fill()
forward(50)
left(90)
goto(-250, 250)
left(180)

forward(510)
# For the basement of the flag
left(90)
forward(50)
right(90)
forward(10)
left(90)
backward(100)
left(90)
forward(10)
right(90)
forward(50)
right(90)
# Going back to main work
backward(10)
left(90)
forward(400)
goto(-250, 0)
end_fill()
home()
# For making sun
color("blue")
goto(-250, 0)
color("red")
goto(-150, -215)
color("white")

# Filling the color of sun
fillcolor("white")
begin_fill()
circle(40)
end_fill()

# Now for making moon
color("red")
goto(-200, -215)
goto(-250, 0)
goto(-200, 65)
color("white")
# dot()

# Function for lining the dot on sequence
def dot_Line(i, j, k):
    while i>=k:
        i=i-1
        goto(-i,j)
        dot()
        print("i and j : ", i, "  ", j)

# Declaring the start value of i, j, k
i = 200
j = 65
k = 136
# To change the value of i, j, k and calling function for multiple times
for l in range(20):
    # Calling Function which draw dot line
    dot_Line(i, j, k)
    i = i-1
    j = j-1
    k = k+1
    print(f"[{l}]value of i and j : ", i,"  ", j)
color("black")
goto(-166, 45)
color("white")
# For making circle of moon
fillcolor("white")
begin_fill()
circle(22, 300)
end_fill()
hideturtle()
goto(-154, 46)
color("red")
home()
# goto(-130, 65)
# color("white")
# dot()




# forward(50)
done()


