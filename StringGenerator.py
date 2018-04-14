rules={'A':'AB','B':'A'}

import sys

a='A'
b='B'

axiom='A'
sentence=''

generation=int(sys.argv[1])

sentence=axiom
# string=axiom
# print(string)

def generate(sent,gen):
	sent=axiom
	string=''
	print('Generation 0 : '+axiom)
	for i in range(gen):
		for char in sent:
			if char is a:
				string+=rules[a]
			elif char is b:
				string+=rules[b]
		sent=string
		string=''
		print('Generation '+str(i+1)+' : '+sent)
	return sent

if __name__=="__main__":
	LString=generate(sentence,generation)
	print("Final "+LString)
