import numpy

a1 = numpy.array([  [1, 1],
		     [2, 5]  ])
		  
b1 = numpy.array([3, 12])

S1 = numpy.linalg.solve(a1, b1)

print "Solution :"
print "x :", S1[0]
print "y :", S1[1]



a2 = numpy.array([  [2, 1, 4],
		     [4, -2, 3],
		     [8, 3, 2]  ])
		    
b2 = numpy.array([16, 9, 20])

S2 = numpy.linalg.solve(a2, b1)

print "Solution :"
print "x :", S2[0]
print "y :", S2[1]
print "z :", S2[2] 
