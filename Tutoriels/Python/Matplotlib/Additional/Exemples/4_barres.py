##### dia 95 #####
plt.bar([1, 2, 3], [30, 10, 40])
plt.show()


##### dia 98 #####
plt.bar([1, 2, 3], [30, 10, 40], align='center')
plt.show()


##### dia 100 #####
plt.bar([1, 2, 3, 4, 5], [30, 10, 40, 20, 55], bottom=20)
plt.show()


##### dia 101 #####
plt.bar([1, 2, 3, 4, 5], [30, 10, 40, 20, 55], bottom=[0, 10, 20, 15, 50])
plt.show()


##### dia 103 #####
plt.bar([1, 2, 3, 4, 5], [30, 10, 40, 20, 55], color='r')
plt.show()


##### dia 104 #####
plt.bar([1, 2, 3, 4, 5], [30, 10, 40, 20, 55], color=['r', 'y', 'g', 'b', 'c'])
plt.show()


##### dia 106 #####
plt.bar([1, 2, 3, 4, 5], [30, 10, 40, 20, 55], color='w', edgecolor=['r', 'y', 'g', 'b', 'c'])
plt.show()


##### dia 108 #####
plt.bar([1, 2, 3, 4, 5], [30, 10, 40, 20, 55], width=1)
plt.show()


##### dia 109 #####
plt.bar([1, 2, 3, 4, 5], [30, 10, 40, 20, 55], width=[0.5, 1, 0.2, 1, 1.5])
plt.show()


##### dia 111 #####
plt.bar([1, 2, 3, 4, 5], [30, 10, 40, 20, 55], linewidth=1)
plt.show()


##### dia 112 #####
plt.bar([1, 2, 3, 4, 5], [30, 10, 40, 20, 55], linewidth=[10, 1, 5, 0, 20])
plt.show()


##### dia 114 #####
plt.bar([1, 2, 3, 4, 5], [30, 10, 40, 20, 55], color='w', xerr=1, yerr=4)
plt.show()


##### dia 116 #####
plt.bar([1, 2, 3, 4, 5], [30, 10, 40, 20, 55], yerr=4, ecolor="k", capsize=20)
plt.show()


##### dia 119 #####
plt.bar([1, 2, 3, 4, 5], [30, 10, 40, 20, 55], align='center')

for i,j in zip([1, 2, 3, 4, 5], [30, 10, 40, 20, 55]) :
	plt.text(i, j+1, str(j), ha='center')
	
plt.show()


##### dia 121 #####
import matplotlib.pyplot as plt

plt.barh([1, 2, 3, 4, 5], [30, 10, 40, 20, 55], align='center', color=["red, "y", "blue", ""white", "m"], xerr=4, ecolor="k", linewidth=5, edgecolor="k", linestyle="dashed")
for i,j in zip([1, 2, 3, 4, 5], [30, 10, 40, 20, 55]) :
	plt.text(3, i, str(j), va="center")
	
plt.title("Exemple d'un diagramme en barres horizontal")
plt.xlabel("Effectifs")
plt.ylabel("Categories")
plt.xticks([1, 2, 3, 4, 5], ["rouge","jaune","bleu","blanc","magenta"], rotation=45)

plt.show()


##### dia 124 #####
plt.bar([1, 2, 3, 4, 5], [30, 10, 40, 20, 55], color='r')
plt.bar([1, 2, 3, 4, 5], [15, 5, 20, 10, 22.5])
plt.show()


##### dia 125 #####
L = [1, 2, 3, 4, 5]
plt.bar(L, [30, 10, 40, 20, 55], color='r')
plt.bar([i-0.5 for i in L], [15, 5, 20, 10, 22.5], alpha=0.5)
plt.show()


##### dia 126 #####
L = [1, 2, 3, 4, 5]
plt.bar(L, [30, 10, 40, 20, 55], color='r', label="Groupe 1")
plt.bar(L, [15, 5, 20, 10, 22.5], bottom=[30, 10, 40, 20, 55], label="Groupe 2")
plt.legend(loc=9)
plt.show()


##### dia 127 #####
plt.bar([1, 2, 3, 4, 5], [30, 10, 40, 20, 55], color='r', width=0.3, label="Groupe 1")
plt.bar([1.30, 2.30, 3.30, 4.30, 5.30], [15, 5, 20, 10, 22.5], width=0.3, label="Groupe 2")
plt.legend(loc=9)
plt.show()
