##### dia 73 #####
M = numpy.array([[2, 3], [3, 3]])
print M

P = numpy.linalg.matrix_power(M, 2)
print P


##### dia 75 #####
M = numpy.array([[2, 3], [3, 3]])
print M

D = numpy.linalg.det(M)
T = numpy.trace(M)

print D
print T


##### dia 77 #####
M = numpy.array([[2, 3], [8, 3]])
print M

V = numpy.linalg.eig(M)
print V

print V[1].T


##### dia 80 #####
a = numpy.array([[3, -1], [2, 3]])
b = numpy.array([1, 19])

S = numpy.linalg.solve(a, b)
print S


##### dia 82 #####
a = numpy.array([[3, 5, -7], [2, -2, 1], [5, -20, 2]])
b = numpy.linalg.solve(a, b)

print S
