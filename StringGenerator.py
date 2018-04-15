import sys

# Boxes
# rules={'F':'F+F-F-F+F'}
# axiom='F'

# Plant
# rules={'X':'F+[[X]-X]-F[-FX]+X','F':'FF'}
# axiom='X'

# Fractal Tree
rules={'F':'FF','0':'F[-0]+0'}
axiom='0'

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
		print('Generation '+str(i+1)+' : '+_sent)
	return _sent