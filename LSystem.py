from StringGenerator import Generate,rules,axiom
from turtle import Turtle,Screen
from Stack import *

turtleStack = Stack()

def draw(_sent,_rules):
	step=5
	angle=25
	turtle=Turtle()
	turtle.speed(0)
	screen=Screen()
	screen.screensize(2000,1500)
	turtle.lt(90)

	for char in _sent:
		if (char is 'F'):
			turtle.pd()
			turtle.fd(step)
		elif(char is '+'):
			turtle.rt(angle)
		elif(char is 'f'):
			turtle.pu()
		elif(char is '['):
			turtleStack.push(turtle.heading())
			turtleStack.push(turtle.pos())
		elif(char is ']'):
			turtle.pu()
			turtle.setposition(turtleStack.pop())
			turtle.setheading(turtleStack.pop())
			turtle.pd()
	screen.exitonclick()


if __name__=="__main__":
	sentence = Generate(axiom,rules)
	draw(sentence,rules)
