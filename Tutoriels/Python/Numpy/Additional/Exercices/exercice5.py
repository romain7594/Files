import numpy

M = numpy.array([  [11, 20, 18, 98],
		    [13, 54, 34, 1],
		    [17, 39, 31, 58],
	 	    [24, 71, 70, 87]  ])
		     
col_split = numpy.hsplit(M, [2])
new = numpy.hstack((col_split[1], col_split[0]))

print M
print new

row_split = numpy.vsplit(new, [2])
new2 = numpy.vstack((row_split[1], row_split[0]))

print new
print new2
