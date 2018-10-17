import numpy

M = numpy.array([   [11, 12, 15],
		    [10, 11, 32],
		    [40, 18, 10]   ])

### Somme cumulee par ligne
cumsum = numpy.cumsum(M, axis=1)
c = ""

for i in cumsum :
	c += str(i)+" "

c = c[:-1]

### Moyenne
moy = numpy.mean(M)

print "Somme cumulee par ligne : ", c
print "Moyenne :", str(moy)



M5 = numpy.array([  [11, 20, 18, 98],
		    [13, 54, 34, 1],
		    [17, 39, 31, 58],
		    [24, 71, 70, 87]   ])
		    

### Somme cumulee par ligne
cumsum5 = numpy.cumsum(M5, axis=1)
c5 = ""

for i in cumsum5 :
	c5 += str(i)+" "

c5 = c5[:-1]


### Moyenne
moy5 = numpy.mean(M5)


print "Somme cumulee par ligne : ", c5
print "Moyenne :", str(moy5)
