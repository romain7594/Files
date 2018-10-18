import matplotlib.pyplot as plt
import random

tirages = []
all = []

for i in range(1000):
	T = sorted([random.randint(1, 50) for i in range(5)])
	tirages.append(T)
	all += T
	
plt.hist(all, bins=[0.5+i for i in range(49)])
plt.xticks(range(1, 49))
plt.xlim(0, 49)

plt.show()
plt.close()

gagnant = sorted([1, 30, 15, 21, 48])

if gagnant in tirages :
	print "Nous avons un gagnant !"
else :
	print "Pas de gagnant aujourd'hui"
