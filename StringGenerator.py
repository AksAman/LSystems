import sys

# Boxes
# rules={'F':'F+F-F-F+F'}
# axiom='F'

# Plant
# rules={'X':'F+[[X]-X]-F[-FX]+X','F':'FF'}
# axiom='X'

# # Fractal Tree
# rules={'F':'FF','0':'F[-0]+0'}
# axiom='0'

# Cantor Set
# axiom='A'
# rules={'A':'AfA','f':'fff'}

# Islands and lakes
# axiom='F+F+F+F'
# rules={'F':'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF','f':'ffffff'}

#FASS Curves
# axiom='A'
# rules={'A':'A+B++B-A--AA-B+','B':'-A+BB++B+A--A-B'}

#Plant B (25.7)
axiom='F'
rules={'F':'F[+F]F[-F]F'}

#Plant C (22.5)
axiom='F'
rules={'F':'FF-[-F+F+F]+[+F-F-F]'}

def Generate(_axiom,_rules):
	_sent=_axiom
	string=''
	rulesList=list(_rules)
	found=False

	if(len(sys.argv) is 1):
		_gens=int(input('Enter the number of generations:'))
	else:
		_gens=int(sys.argv[1])
	print('Generation 0 : '+axiom)
	for i in range(_gens):
		for char in _sent:
			for rule in range(len(_rules)):
				if char is rulesList[rule]:
					string+=rules[rulesList[rule]]
					found=True
			if(not found):
				string+=char
			found=False
		_sent=string
		string=''
		# print('Generation '+str(i+1)+' : '+_sent)
	return _sent