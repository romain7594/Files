import numpy
import random

M = numpy.eye(5)

for i in M :
	for j in range(len(i)) :
		if i[j] == 0 :
			i[j] = random.randint(0, 10)

print M			
