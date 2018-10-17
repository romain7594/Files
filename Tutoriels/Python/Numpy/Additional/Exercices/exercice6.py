import numpy

M = numpy.array([  [35, 40],
		    [78, 98]  ])
		    
D = numpy.linalg.det(M)
T = numpy.trace(M)

print "Determinant :", D
print "Trace :", T
