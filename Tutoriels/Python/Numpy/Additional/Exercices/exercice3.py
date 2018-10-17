import numpy

M = numpy.array([   [11, 12, 15],
		    [10, 11, 32],
		    [40, 18, 10]   ])

tmp = numpy.vsplit(M, [1:])

premiere_ligne = tmp[0]
lignes_suivantes = tmp[1]
