#!/usr/bin/env python
#-*- coding: utf-8 -*-

##### Fonctions de lecture d'un fichier fasta

# Fasta 1 sequence

"""
Entree : fichier fasta
Sortie : id sequence, sequence
"""
def readfasta(fichier):
	lefichier = open(fichier,'r')
	sequence = ""
	lines = lefichier.readlines()
	lefichier.close()

	for x in lines[1:]:
		sequence = sequence+x[:-1]

	return lines[0][1:-1], sequence




# Fasta multiple sequences

"""
Entree : fichier fasta
Sortie : liste [nom seq, sequence]
"""
def readfasta(fichier):
	lefichier = open(fichier,'r')
	lines = lefichier.readlines()
	lefichier.close()

	listeseq, nom, seq = [], "", ""

	for i in lines:
		if i[0] == '>':
			if seq != "":
				tup = (nom, seq)
				listeseq.append(tup)
				nom, seq = "", ""
			
			nom +=i [1:-1]
		else:
			seq +=i [:-1]

	tup = (nom,seq)
	listeseq.append(tup)

	return listeseq




"""
Entree : fichier fasta
Sortie : dictionnaire (clés : id sequence, valeur : sequence)
"""
def readfasta2(fichier):
	seq, tmp, cle = {}, "", ""

	fi = open(fichier,'r')
	line = fi.readline()
	
	while line != '' :
		if line[0] == '>':
			if tmp != '' :
				seq[cle] = tmp
				tmp = ""

			cle = line[:-1].split('_')[1]
		else:
			tmp += line[:-1]
		
		line = fi.readline()
	
	seq[cle] = tmp
	fi.close()

	return seq
