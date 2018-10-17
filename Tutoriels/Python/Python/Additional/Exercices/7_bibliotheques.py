##### 1 #####
import numpy

M = numpy.zeros((9, 9))

print M


##### 2 #####
import random

for i in range(len(M)):
	for j in range(len(M[i])):
		M[i][j] = random.randint(0, 101)
		
print M


##### 3 #####
L = M[1]

print M
print L


##### 4 #####
mid = len(L)/2
L[mid] = random.randint(0, 101)

print L


##### 5 #####
print M
print L


##### 6 #####
import matplotlib.pyplot as plt

x = M[0]
y = M[-1]

plt.plot(x, y)
plt.show()
