#!/usr/bin/python
#-*- coding: utf-8 -*-

import copy
import matplotlib.pyplot as plt
import kmedoides

# Fonction de calcul de la silhouette
"""
Entree : liste des groupes, dicionnaire {identifiant : vecteur valeurs}, metrique
Sortie : liste de la valeur silhouette pour chaque organisme, moyenne des silhouettes
"""
def silhouette(groupes, matrice, metrique):
	S = []

	for G in range(len(groupes)):
		S.append([])
		groupesbis = copy.deepcopy(groupes)
		groupesbis.remove(groupes[G])

		for i in groupes[G]:
			liste = copy.deepcopy(groupes[G])
			liste.remove(i)
	
			### Calcul de ai ###
			ai = 0

			for l in liste:
				ai = ai+metrique(matrice[i], matrice[l])
			
			if len(liste) != 0:
				ai = ai/float(len(liste))
			
			### Calcul de bi ###
			liste_bi = []
			for m in groupesbis:
				bi = 0

				for n in m:
					bi += metrique(matrice[i], matrice[n])
			
				bi = bi/float(len(m))
				liste_bi.append(bi)
			
			bi = min(liste_bi)
			si = (bi-ai)/max(ai, bi)
			
			S[G].append(si)
	
	Moyenne = 0.0
	L = 0
	
	for y in S:
		L = L+len(y)

		for w in y:
			Moyenne = Moyenne+w
		
	Moyenne = Moyenne/L

	return S, Moyenne




# Plot silhouette
"""
Entree : liste des silhouettes, moyenne (obtenues avec la fonction silhouette())
Sortie : graphe
"""
def plot_silhouette(donnees, moyenne):
	colors = ['b', 'r', 'y', 'c', 'm', 'g']
	if len(donnees) > len(colors):
		while len(donnees) > len(colors):
			colors += colors

	width = 1
	L = []
	c = 0

	for l in donnees:
		for t in l:
			L.append(c)
			c = c+1
	
	#plt.xlim([-1, 1])

	for i in range(len(donnees)):
		plt.barh(L[0:len(donnees[i])], donnees[i], width, color=colors[i], align='center')
		
		for x in range(len(donnees[i])):
			L.remove(L[0])
	
	plt.axvline(moyenne, color = 'k', linewidth=1.5, linestyle="--")
	plt.yticks([])
	plt.xlabel("Silhouette", size=15)
	plt.ylabel("Clusters", size=15)
	plt.show()
	plt.close()




# Silhouette en fonction du nombre de clusters
"""
Entree : liste des k à tester, dictionnaire {identifiant : vecteur valeurs}, metrique, 1 pour plot chaque k
Sortie : iste des valeurs de k ordonnées selon une valeur silhouette décroissante
"""
def silhouette_k(liste_k, matrice, metrique, c):
	Means = []
	
	for k in liste_k:
                clusters = kmedoides.kmedoides(matrice, k, metrique)
		Si, M = silhouette(clusters, matrice, metrique)
		Means.append(M)
	
	if c == 1:
		plt.plot(liste_k, Means, marker="o")
                plt.xticks(liste_k)
                plt.grid()
		plt.xlabel("Nombre de clusters", size=15)
		plt.ylabel("Silhouette", size=15)
		plt.show()
		plt.close()
	
	for i in range(len(Means)):
		Means[i] = [Means[i], i+2]
	
	Means = sorted(Means, reverse=True)
	best_k = []

	for m in Means:
		best_k.append(m[1])
			
	return best_k
