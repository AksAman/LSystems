rules={'A':'AB','B':'A'}

import sys

a='A'
b='B'

axiom='A'
sentence=''


if(len(sys.argv) is 1):
	generation=int(input('Enter the number of generations:'))
else:
	generation=int(sys.argv[1])


def generate(_sent,_gen,_rules):
	_sent=axiom
	string=''
	rulesList=list(_rules)

	print('Generation 0 : '+axiom)
	for i in range(_gen):
		for char in _sent:
			for rule in range(len(_rules)):
				if char is rulesList[rule]:
					string+=rules[rulesList[rule]]

		_sent=string
		string=''
		print('Generation '+str(i+1)+' : '+_sent)
	return _sent


if __name__=="__main__":
	LString=generate(sentence,generation,rules)
	print("Final "+LString)