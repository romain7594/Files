##### dia 17 #####
L = [[1, 2, 3], [4, 5, 6]]
print L[1][0]

M = numpy.array(L)
print M[1][0]
print M[1,0]


##### dia 19 #####
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print L[0]
print L[2]

M = numpy.array(L)
print M[0]
print M[0,:]
print M[2]
print M[2,:]


#####  dia 21 #####
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

M = numpy.array(L)
print M
print M[1:3,:]
print M[1:3]


##### dia 23 #####
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

M = numpy.array(L)
print M
print M[:,1]


##### dia 25 #####
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

M = numpy.array(L)
print M
print M[:,0:2]
