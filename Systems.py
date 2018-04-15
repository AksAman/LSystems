Koch Curve
rules={'F':'F+F-F-F+F'}
axiom='F'

Plant
rules={'X':'F+[[X]-X]-F[-FX]+X','F':'FF'}
axiom='X'

Fractal Tree
rules={'F':'FF','0':'F[-0]+0'}
axiom='0'

Cantor Set
axiom='A'
rules={'A':'AfA','f':'fff'}

Islands and lakes
axiom='F+F+F+F'
rules={'F':'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF','f':'ffffff'}

FASS Curves
axiom='A'
rules={'A':'A+B++B-A--AA-B+','B':'-A+BB++B+A--A-B'}

Plant B (25.7)
axiom='F'
rules={'F':'F[+F]F[-F]F'}

axiom='F'
rules={'F':'FF-[-F+F+F]+[+F-F-F]'}
