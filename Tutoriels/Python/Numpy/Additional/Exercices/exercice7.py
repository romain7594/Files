import numpy

M = numpy.array([  [35, 40],
		    [78, 98]  ])
		    
V = numpy.linalg.eig(M)
tmp = V[1].T

val_propres = V[0]
vect_propres = [tmp[0,], tmp[1,]]

print "Valeurs propres :", val_propres[0], val_propres[1]
print "Vecteurs propres :", vect_propres[0], vect_propres[1]
