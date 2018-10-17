##### dia 131 #####
import matplotlib.pyplot as plt
import random

D = [random.randint(1, 6) for i in range(1000)]
plt.hist(D, 6)

plt.show()


##### dia 134 #####
D = [random.randint(1, 6) for i in range(1000)]

plt.hist(D, 6, histtype='step')

plt.show()


##### dia 135 #####
D = [random.randint(1, 6) for i in range(1000)]

plt.hist(D, 6, histtype='stepfilled')

plt.show()


##### dia 137 #####
D = [random.randint(1, 6) for i in range(100)]
D2 = [random.randint(1, 6) for i in range(100)]
D3 = [random.randint(1, 6) for i in range(100)]

plt.hist(D, 6)
plt.hist(D2, 6)
plt.hist(D3, 6)

plt.show()


##### dia 138 #####
D = [random.randint(1, 6) for i in range(100)]
D2 = [random.randint(1, 6) for i in range(100)]
D3 = [random.randint(1, 6) for i in range(100)]

plt.hist([D, D2, D3], 6, histtype='barstacked')

plt.show()


##### dia 139 #####
D = [random.randint(1, 6) for i in range(100)]
D2 = [random.randint(1, 6) for i in range(100)]
D3 = [random.randint(1, 6) for i in range(100)]

plt.hist([D, D2, D3], 6)

plt.show()


##### dia 141 #####
D = [random.randint(1, 6) for i in range(1000)]

plt.hist(D, 6, bottom=30)

plt.show()


##### dia 142 #####
D = [random.randint(1, 6) for i in range(1000)]

plt.hist(D, 6, bottom=[0, 0, 0, 10, 20, 50])

plt.show()


##### dia 144 #####
D = [random.randint(1, 6) for i in range(1000)]
D2 = [random.randint(1, 6) for i in range(1000)]

plt.hist([D, D2], 6, label=["Tirage 1", "Tirage 2"])

plt.legend()
plt.title("Lances de de")
plt.xlabel("Chiffres sortis")
plt.xlabel("Effectif")

plt.show()


##### dia 146 #####
D = [random.randint(1, 6) for i in range(1000)]

plt.hist(D, bins=[0.5+i for i in range(7)])
plt.xticks(range(1, 7))
plt.xlim(0, 7)
plt.show()


##### dia 148 #####
p = [random.randint(1, 6) for i in range(1000)]

plt.hist(p, [0.5+i for i in range(7)])
L = super_fonction_de_comptage(p)

for a,b in zip(L, range(1, 7)):
	plt.text(b, a+1, str(a), ha='center')
	
plt.show()


##### dia 149 #####
def super_fonction_de_comptage(liste):
	dico = {}
	for i in liste :
		if dico.has_key(str(i)) :
			dico[str(i)] += 1
		else:
			dico[str(i)] = 1
	
	D = dico.items()
	for j in range(len(D)):
		D[j] = [int(D[j][0]), D[j]]
	
	D = sorted(D)
	for k in range(len(D)) :
		D[k] = D[k][1][1]
	
	return D
