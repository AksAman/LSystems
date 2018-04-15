Curves = {
	'Koch Curve':{
				'axiom':'F',
				'rules':{'F':'F+F-F-F+F'},
				'angle':90
	},

	'Plant':{
				'axiom':'X',
				'rules':{'X':'F+[[X]-X]-F[-FX]+X','F':'FF'},
				'angle':25
	},

	'Circuit':{
				'axiom':'X',
				'rules':{'X':'F+[[X]-X]-F[-FX]+X','F':'FF'},
				'angle':45
	},

	'Fractal Tree':{
				'axiom':'0',
				'rules':{'F':'FF','0':'F[-0]+0'},
				'angle':45
	},

	'Cantor Set':{
				'axiom':'A',
				'rules':{'A':'AfA','f':'fff'},
				'angle':90
	},

	'Islands and lakes':{
				'axiom':'F+F+F+F',
				'rules':{'F':'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF','f':'ffffff'},
				'angle':90
	},

	'FASS Curves':{
				'axiom':'A',
				'rules':{'A':'A+B++B-A--AA-B+','B':'-A+BB++B+A--A-B'},
				'angle':60
	},
	'Plant B':{
				'axiom':'F',
				'rules':{'F':'F[+F]F[-F]F'},
				'angle':25.7
	},
	'Plant C':{
				'axiom':'F',
				'rules':{'F':'FF-[-F+F+F]+[+F-F-F]'},
				'angle':22.5
	},
}