#!/usr/bin/python
#-*- coding: utf-8 -*-

import random
import copy

# Initialisation des k groupes
"""
Entree : dictionnaire {identifiant : vecteur valeurs}, nombre de clusters k, mesure de dissimilarité
Sortie : Liste des groupes formés
"""
def initialise_k_group(dico, k, metrique):
	identifiant = dico.keys() ### identifiants
	groupes = []
	
	### Choix des k centres ###
	for i in range(k):
		C = random.choice(identifiant)
		groupes.append([C])
		identifiant.remove(C)
	
	### Calcul des distances ###
	for j in range(len(identifiant)):
		distance = []

		for l in range(len(groupes)):
			D = metrique(dico[groupes[l][0]], dico[identifiant[j]])

			distance.append([D, l, identifiant[j]])
				   # [distance, indice du groupe, nom de l'identifiant]
		
		distance = sorted(distance)
		groupes[distance[0][1]].append(distance[0][2])
		# liste de liste (groupes)

	return groupes




# Recherche du meilleur centre d'un groupe
"""
Entree : un cluster (liste), dictionnaire {identifiant : vecteur valeurs}, mesure de dissimilartié
Sortie : meilleur centre
"""
def meilleur_centre(cluster, dico_matrice, metrique):
	liste_moy = []

	for ident in range(len(cluster)):
		to_do_list = copy.deepcopy(cluster)
		to_do_list.remove(cluster[ident])
		M = 0.0

		for x in to_do_list:
			M += metrique(dico_matrice[cluster[ident]], dico_matrice[x])
		
		if len(to_do_list) != 0:
			liste_moy.append([M/len(to_do_list), cluster[ident]])
		
		else:
			liste_moy.append([M, cluster[ident]])
	
	liste_moy = sorted(liste_moy)
	
	return liste_moy[0][1]




# Re-clustering des clusters
"""
Entree : clusters, dictionnaire {identifiant : vecteur valeurs}, mesure de dissimilarité
Sortie : nouveaux groupes
"""
def refaire_group(clusters, dico_matrice, metrique):
	new_group = []
	identifiant = dico_matrice.keys()
	
	for x in range(len(clusters)):
		new_group.append([meilleur_centre(clusters[x], dico_matrice, metrique)])
		identifiant.remove(new_group[x][0])	

	### Calcul des distances ###
	for j in range(len(identifiant)):
		distance = []

		for l in range(len(new_group)):
			D = metrique(dico_matrice[new_group[l][0]], dico_matrice[identifiant[j]])

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




# Fonction k-medoides
"""
Entree : dictionnaire {identifiant : vecteur valeurs}, nombre de clusters k, mesure de dissimilarité
Sortie : groupes
"""
def kmedoides(D, k, methode):
        Clusters1 = initialise_k_group(D, k, methode)                    
	Clusters = converge(Clusters1, D, methode)
        
        return Clusters
