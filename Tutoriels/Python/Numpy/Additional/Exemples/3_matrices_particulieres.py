##### dia 87 #####
A = numpy.arange(10)
print A

A = numpy.arange(3, 17)
print A

A = numpy.arange(0, 20, 2)
print A


##### dia 31 #####
A = numpy.linspace(1, 50)
print A

B = numpy.linspace(10, 20, 14)
#B = numpy.linspace(10, 20, num=14)
print B


##### dia 33 #####
A = numpy.random.rand(5)
print A

B = numpy.random.rand(10)
print B

A = numpy.random.rand(4, 6)
print A

A = numpy.random.randint(10, size=4)
print A

B = numpy.random.randint(10, size=(3, 5))
print B

A = numpy.random.randint(10, 20, size=8)
print A

B = numpy.random.randint(5, 100, size=(5, 5))
print B
