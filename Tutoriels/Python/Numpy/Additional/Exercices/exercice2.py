import numpy

M = numpy.array([   [11, 12, 15],
		     [10, 11, 32],
		     [40, 18, 10]   ])
dico_indice = {}
k = 0

for i in range(len(M)) :
	for j in range(len(M[i])) :
		dico_indice[str(i)+"."+str(j)] = k
		k += 1
		
indice_nombre = dico_indice.items()
dico_indice = {}

for i in indice_nombre :
	dico_indice[i[1]] = [int(i[0].split(".")[0]), int(i[0].split(".")[1])]

mini = numpy.argmin(M)
maxi = numpy.argmax(M)

val_mini = M[dico_indice[mini][0], dico_indice[mini][1]]
val_maxi = M[dico_indice[maxi][0], dico_indice[maxi][1]]

indice_mini = []
indice_maxi = []

for i in range(M.shape[0]):
	for j in range(M.shape[1]):
		if M[i,j] == val_mini :
			indice_mini.append([i,j])
		
		if M[i,j] == val_maxi :
			indice_maxi.append([i,j])
			
print M
print indice_mini
print indice_maxi
