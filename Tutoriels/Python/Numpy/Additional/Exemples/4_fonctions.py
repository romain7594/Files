##### dia 36 #####
M = numpy.array([[1, 2, 3, 4], [5, 6, 7, 9]])
print M

M2 = M.T
#M2 = M.transpose()
#M2 = numpy.transpose(M)
print M2


##### dia 38 #####
M = numpy.array([[1, 2, 3, 4], [5, 6, 7, 9]])
print M.shape
print M.shape[0]
print M.shape[1]

M = numpy.array([1, 2, 3, 4])
print M2.shape
print M2.shape[0]
print M2.shape[1]

M = numpy.array([[1], [2], [3], [4]])
print M3.shape
print M3.shape[0]
print M3.shape[1]


##### dia 40 #####
M1 = numpy.array([[1, 2], [3, 4]])
M2 = numpy.array([[2, 5], [2, 4]])

print M1*M2


##### dia 42 #####
M1 = numpy.array([[1, 2], [3, 4]])
M2 = numpy.array([[2, 5], [2, 4]])

R = numpy.dot(M1, M2)

print R

M1 = numpy.array([[1, 2, 3], [3, 4, 6]])
M2 = numpy.array([[2, 5], [2, 4]])

R = numpy.dot(M1, M2)


##### dia 44 #####
A = numpy.minimum(34, 12)
print A

A = numpy.minimum([1, 4, 3], [12, 1, 19])
pprint A

M1 = numpy.array([[14, 1, 13], [12, 11, 10]])
M2 = numpy.array([[11, 2, 15], [2, 17, 9]])

B = numpy.minimum(M1, M2)
print B

M = numpy.array([[12, 14, 11, 18], [12, 10, 14, 16]])

A = numpy.minimum(M, 13)
print A


##### dia 46 #####
M = numpy.array([12, 14, 11, 18])

I = numpy.argmin(M)
#I = M.argmin()
print I

M = numpy.array([[12, 14, 11], [10, 1, 30]])

I = numpy.argmin(M)
print I


##### dia 47 #####
M = numpy.random.randint(100, size=(5, 6))
print M

I = numpy.argmin(M, axis=0)
#I = M.argmin(0)
print I

M = numpy.random.randint(100, size=(5, 6))
print M

I = numpy.argmin(M, axis=1)
print I


##### dia 49 #####
N = 1.78756467
R = numpy.round(N)
#R = numpy.around(N)

print R

N = 1.78756467
R = numpy.round(N, 2)

print R

N = 1.3
R = numpy.ceil(N)

print R

N = 1.7
R = numpy.floor(N)

print R


##### dia 51 #####
M = numpy.random.randint(100, size=(3, 4))
print M

S = numpy.sort(M)
print S

M = numpy.random.randint(100, size=(3, 4))
print M

S = numpy.sort(M, 0)
print S


##### dia 52 #####
M = numpy.random.randint(100, size=(3, 4))
print M

S = numpy.sort(M, 1)
print S


##### dia 55 #####
M = numpy.random.randint(100, size=(2, 4))
print M

S = numpy.sum(M)
print S

M = numpy.random.randint(100, size=(2, 4))
print M

S = numpy.sum(M, axis=0)
#S = numpy.sum(M, 0)
print S

M = numpy.random.randint(100, size=(2, 4))
print M

S = numpy.sum(M, axis=1)
print S


##### dia 56 #####
M = numpy.random.randint(100, size=(2, 2))
print M

S = numpy.prod(M)
print S

M = numpy.random.randint(100, size=(2, 2))
print M

S = numpy.prod(M, axis=0)
print S

M = numpy.random.randint(100, size=(2, 2))
print M

S = numpy.prod(M, axis=1)
print S


##### dia 57 #####
M = numpy.random.randint(100, size=(2, 2))
print M

S = numpy.cumsum(M)
print S

M = numpy.random.randint(100, size=(2, 2))
print M

S = numpy.cumsum(M, axis=0)
print S

M = numpy.random.randint(100, size=(2, 2))
print M

S = numpy.cumsum(M, axis=1)
print S


##### dia 58 #####
M = numpy.random.randint(100, size=(2, 2))
print M

S = numpy.mean(M)
print S

M = numpy.random.randint(100, size=(2, 2))
print M

S = numpy.mean(M, axis=0)
print S

M = numpy.random.randint(100, size=(2, 2))
print M

S = numpy.mean(M, axis=1)
print S


##### dia 60 #####
a = numpy.array([1, 2, 3])
b = numpy.array([4, 5, 6])

H = numpy.hstack((a, b))
V = numpy.vstack((a, b))

print H
print V


##### dia 63 #####
M = numpy.random.randint(10, size=(4,4))
print M

H = numpy.hsplit(M, 2)
#H = numpy.split(M, 2, axis=1)$
print H


##### dia 64 #####
M = numpy.random.randint(10, size=(4,4))
print M

V = numpy.vsplit(M, 4)
#V = numpy.vsplit(M, 4, axis=0)
print V

M = numpy.random.randint(10, size=(3,7))
print M

H = numpy.hsplit(M, [2, 4, 6])
print H


##### dia 65 #####
M = numpy.random.randint(10, size=(8,7))
print M

V = numpy.vsplit(M, [2, 4, 5])
print V

M = numpy.random.randint(10, size=(4, 4))
print M

V = numpy.vsplit(M, 3)
print V


##### dia 67 #####
M1 = numpy.random.randint(100, size=(2, 2))
print M1

W = numpy.where(M1>20, 0, 1)
print W

M1 = numpy.random.randint(100, size=(2, 2))
M2 = numpy.random.randint(100, size=(2, 2))

print M1
print M2

W = numpy.where(M1<M2, 0, 1)
print W


##### dia 68 #####
M1 = numpy.random.randint(100, size=(2, 2))
M2 = numpy.random.randint(100, size=(2, 2))

print M1
print M2

print M1>20
print M1<M2

M1 = numpy.random.randint(100, size=(2, 2))
M2 = numpy.random.randint(100, size=(2, 3))

print M1
print M2

W = numpy.where(M1>M2, 0, 1)
print W
