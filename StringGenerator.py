import sys
from Systems import Curves

axiom='0'
rules={'F':'FF','0':'F[-0]+0'}

def Generate():
	curve=AskCurves()
	_System=Curves[curve]
	sent=_System['axiom']
	_rules=_System['rules']
	print('Rules '+str(_rules))
	_string=''
	_rulesList=list(_rules)
	_found=False
	print('Selected system of curves is:'+curve)
	_gens=TakeInput()
	# print('Generation 0 : '+axiom)
	for i in range(_gens):
		for char in sent:
			for rule in range(len(_rules)):
				if char is _rulesList[rule]:
					_string+=_rules[_rulesList[rule]]
					_found=True
			if(not _found):
				_string+=char
			_found=False
		sent=_string
		_string=''
		# print('Generation '+str(i+1)+' : '+sent)
	return [sent,_System['angle']]


def TakeInput():
	if(len(sys.argv) is 1):
		return int(input('Enter the number of generations:'))
	else:
		return int(sys.argv[1])


def AskCurves():
	print ('Which curve you need to visualize: ')
	i=0
	_curveList=[]
	for nameKey in Curves.keys():
		_curveList.append(nameKey)

	print ("List:"+str(_curveList))

	for curve in _curveList:
		print(str(i+1)+' : '+curve)
		i+=1

	_curveInput=int(input('Curve index:'))-1
	return _curveList[_curveInput]
