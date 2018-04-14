rules={'A':'AB','B':'A'}

import sys

axiom='A'
sentence=''


if(len(sys.argv) is 1):
	generations=int(input('Enter the number of generations:'))
else:
	generations=int(sys.argv[1])


def Generate(_axiom,_gens,_rules,_sent):
	_sent=_axiom
	string=''
	rulesList=list(_rules)

	print('Generation 0 : '+axiom)
	for i in range(_gens):
		for char in _sent:
			for rule in range(len(_rules)):
				if char is rulesList[rule]:
					string+=rules[rulesList[rule]]
		_sent=string
		string=''
		print('Generation '+str(i+1)+' : '+_sent)
	return _sent


if __name__=="__main__":
	LString=generate(axiom,generations,rules,sentence)
	print("Final "+LString)