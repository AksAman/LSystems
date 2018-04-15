from StringGenerator import Generate,rules,axiom
from turtle import Turtle,Screen
from Stack import *

turtleStack = Stack()

def draw(_sent,_rules):
	step=5
	angle=90
	turtle=Turtle()
	turtle.speed(0)
	screen=Screen()
	# screen.title('L-System visualisation for '+str(_gens)+' generations.')
	screen.screensize(2000,1500)
	turtle.lt(90)

	for char in _sent:
		if (char is 'F'):
			turtle.fd(step)
		elif(char is '+'):
			turtle.rt(angle)
		elif(char is '-'):
			turtle.lt(angle)
	screen.exitonclick()


if __name__=="__main__":
	sentence = Generate(axiom,rules)
	draw(sentence,rules)
