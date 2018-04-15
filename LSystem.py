from StringGenerator import Generate,rules,axiom
from turtle import Turtle,Screen
from Stack import *

turtleStack = Stack()

def draw(_sent,_angle):
	step=8
	angle=_angle
	turtle=Turtle()
	turtle.hideturtle()
	turtle.speed(0)
	screen=Screen()
	screen.screensize(2000,1500)
	turtle.lt(90)
	# turtle.onclick(turtle.update())

	for char in _sent:
		if (char is 'F' or char is 'A' or char is 'B'):
			turtle.pd()
			turtle.fd(step)
		elif(char is '-'):
			turtle.rt(angle)
		elif(char is '+'):
			turtle.lt(angle)
		elif(char is 'f'):
			turtle.pu()
			turtle.fd(step)
		elif(char is '['):
			turtleStack.push(turtle.heading())
			turtleStack.push(turtle.pos())
		elif(char is ']'):
			turtle.pu()
			turtle.setposition(turtleStack.pop())
			turtle.setheading(turtleStack.pop())
			turtle.pd()
		elif(char is '0'):
			turtle.fd(step/2)
	screen.exitonclick()


if __name__=="__main__":
	ruleAngle=Generate()
	sentence = ruleAngle[0]
	angle=ruleAngle[1]
	draw(sentence,angle)
