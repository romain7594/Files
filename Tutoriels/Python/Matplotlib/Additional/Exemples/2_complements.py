##### dia 52 #####
plt.plot([0, 2], [3, 1], label="Courbe 1")
plt.plot([0, 2], [6, 2], label="Courbe 2")

plt.show()


##### dia 56 #####
plt.plot([0, 2], [3, 1])
plt.plot([0, 2], [6, 2])

plt.title("Voici un\nexemple")
plt.xlabel("Axe des x")
plt.ylabel("Axe des y")

plt.show()


##### dia 59 #####
x, y = 1, 1
plt.plot(x, y, "o")

plt.text(1.005, 1.005, "Point de coordonnees ("+str(x)+","+str(y)+")")
plt.text(1, 1.04, "Ceci est du texte")

plt.show()


##### dia 60 #####
x = range(10)
y = [random.randint(0, 10) for i in range(10)]

for a,b in zip(x,y):
	plt.plot(a, b, "o")
	plt.text(a+0.25, b+0.1, "x : "+str(a))
	plt.text(a+0.25, b+0.2, "y : "+str(b))
	
plt.show()


##### dia 63 #####
plt.plot(1, 1)

plt.text(1, 1, "Jaune", color="y")
plt.text(1, 1.01, "Bleu", color=b")
plt.text(1, 1.02, "Rouge", color="r")

plt.show()


##### dia 65 #####
plt.plot(1, 1)

plt.text(1, 1, "Taille 10", size=10)
plt.text(1, 1.01, "Taille 20", size=10)
plt.text(1, 1.02, "Taille xx-large", size="xx-large")
plt.text(0.96, 0.96, "Taille 50", size=50)
plt.text(0.96, 1.04, "Taille medium", size='medium')

plt.show()


##### dia 67 #####
plt.plot(1, 1)

plt.text(1, 1.01, "horizontal")
plt.text(1, 1, "vertical", rotation="vertical")
plt.text(0.98, 1, "90 degres", rotation=90)
plt.text(1, 0.99, "45 degres", rotation=45)
plt.text(1, 01, 0.99, "75 degres", rotation=75)

plt.show()


##### dia 69 #####
plt.plot(1, 1)

plt.text(1, 1, "normal", size=40)
plt.text(1, 1.02, "italique", style='italic', size=40)
plt.text(1, 0.98, "oblique", style="oblique", size=40)

plt.show()


##### dia 71 #####
plt.plot(1, 1)

plt.text(1, 1, "AV centre", va='center')
plt.text(1, 1, "AH droite", horizontalalignment="right")

plt.show()


##### dia 75 #####
plt.plot(1, 1, "o")
plt.plot(2, 2, "o")
plt.plot(3, 3, "o")

plt.xlim(0, 5)
plt.ylim(ymin=0, ymax=6)
#plt.axis([0, 5, 0, 6])

plt.show()


##### dia 77 #####
plt.plot(range(5), range(5))
plt.xticks(range(1, 5, 1), ["Graduation", "axe", "des", "x"])
plt.yticks(range(4, 0, -1), ["Graduation", "axe", "des", "y"], rotation=45)

plt.show()


##### dia 81 #####
plt.axvline(2, c='r', linestyle="--")
plt.axhline(3, lw=10)
plt.axvline(x=1.95, ymin=0.25, ymax=0.75, c="k", lw=10)
plt.axhline(y=2.95, xmin=0.25, xmax=0.75, c="g", linestyle=":", lw=5)

plt.show()


##### dia 84 #####
plt.axis([0, 10, 0, 10])

plt.axhspan(2, 3)
plt.axvspan(5, 6, alpha=0.7, color='y', hatch='/')
plt.axvspan(1, 2, 0.10, 0.75, fill=False, color='r', lw=5)
plt.axhspan(4, 5, 0.30, 1, fill=False, color='k', hatch='*')
plt.axhspan(7, 8, 0, 0.75, linestyle='dashed', fill=False, color='green', lw=5)

plt.show()


##### dia 86 #####
plt.axis([0, 10, 0, 10])

plt.plot([0, 10], [0, 10])

plt.grid(True)
plt.show()


##### dia 87 #####
plt.axis([0, 10, 0, 10])

plt.plot([0, 10], [0, 10])

plt.grid(True, axis='x', linestyle='-')
plt.show()
