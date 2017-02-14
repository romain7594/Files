#!/usr/bin/python
#-*- coding: utf-8 -*-

import random
import copy

# Initialisation des k groupes
"""
Entree : dictionnaire {identifiant : vecteur valeurs, mesure de dissimilarité, liste des centres (= k)
Sortie : Liste des groupes formés
"""
def initialise_k_group(dico, metrique, centres):
	identifiant = dico.keys() ### identifiants
	groupes = [[] for i in range(len(centres))]

	### Calcul des distances ###
	for j in range(len(identifiant)):
		distance = []

		for l in range(len(centres)):
			D = metrique(centres[l], dico[identifiant[j]])

			distance.append([D, l, identifiant[j]])
				   # [distance, indice du groupe, nom de l'identifiant]
		
		distance = sorted(distance)
		groupes[distance[0][1]].append(distance[0][2])
		# liste de liste (groupes)

	return groupes




# Recherche du vecteur moyen d'un cluster
"""
Entree : un cluster (liste), dictionnaire {identifiant : vecteur valeurs}
Sortie : vecteur moyen
"""
def moyenne_groupe(cluster, dico_matrice):
	vect_moy = [0 for i in range(len(dico_matrice[dico_matrice.keys()[0]]))]

	for i in cluster :
		for j in range(len(vect_moy)):
			vect_moy[j] += float(dico_matrice[i][j])
		
	vect_moy2 = [p/len(cluster) for p in vect_moy]
	
	return vect_moy2




# Re-clustering des clusters
"""
Entree : clusters, dictionnaire {identifiant : vecteur valeurs}, mesure de dissimilarité
Sortie : nouveaux groupes
"""
def refaire_group(clusters, dico_matrice, metrique):
	centres = []
	new_group = [[] for i in range(len(clusters))]
	identifiant = dico_matrice.keys()

	for x in clusters:
		centres.append(moyenne_groupe(x, dico_matrice))

	### Calcul des distances ###
	for j in range(len(identifiant)):
		distance = []

		for l in range(len(centres)):
			D = metrique(centres[l], dico_matrice[identifiant[j]])

			distance.append([D, l, identifiant[j]])
					#[distance, indice du groupe, identifiant]
		
		distance = sorted(distance)
		new_group[distance[0][1]].append(distance[0][2])
		# liste de liste (groupes)
	
	return new_group




# Clustering jusqu'à convergence
"""
Entree : clusters, dictionnaire {identifiant : vecteur valeurs}, mesure de dissimilarité
Sortie : nouveaux group
"""
def converge(groups, dico_matrice, distance):
	new_groups = refaire_group(groups, dico_matrice, distance)

	for i in range(len(groups)):
		groups[i] = sorted(groups[i])
		new_groups[i] = sorted(new_groups[i])

	new_groups = sorted(new_groups)
	groups = sorted(groups)
	
	# Itération jusqu'à convergence
	while new_groups != groups:
		groups = new_groups
		new_groups = refaire_group(groups, dico_matrice, distance)

		for i in range(len(new_groups)):
			new_groups[i] = sorted(new_groups[i])

		new_groups = sorted(new_groups)

	return new_groups




# Fonction k-means
"""
Entree : dictionnaire {identifiant : vecteur valeurs}, mesure de dissimilarité, liste des centres (= k)
Sortie : groupes
"""
def kmeans(D, methode, centres):
        Clusters1 = initialise_k_group(D, methode, centres)         
	Clusters = converge(Clusters1, D, methode)
        
        return Clusters
