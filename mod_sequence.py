#!/usr/bin/env python
#-*- coding: utf-8 -*-

##### Fonctions de modification de sequences

# Complémentaire d'une sequence
"""
Entree : sequence (chaine de caracteres)
Sortie : chaine de caracteres
"""
def complementaire(sequence):
	D = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
	seq = ""

	for i in sequence :
		seq += D[i]
	
	return seq




# Inverse une sequence
"""
Entree : sequence (chaine de caracteres)
Sortie : chaine de caracteres
"""
def reverse_seq(sequence):
	seq = ""

	for i in range(len(sequence)-1, -1, -1):
		seq += sequence[i]
	
	return seq
