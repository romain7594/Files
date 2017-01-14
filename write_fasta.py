#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Fonctions d'écriture de fichier fasta

"""
Entree : liste id sequences, liste sequences, nom fichier sortie
Sortie : fichier fasta
"""
def WriteFasta(name, sequences, file_out):
	f = open(file_out, 'w')
	
	for seq in range(len(sequences)) :
		f.write(">"+name[seq]+"\n")
		
		taille = len(sequences[seq])

		if taille > 80 :
			for j in range(0, taille, 80):
				if j+80 > taille :
					f.write(sequences[seq][j:taille])
			
				else :
					f.write(sequences[seq][j:j+80])
			
				f.write("\n")
			
		else :
			f.write(sequences[seq]+"\n")
		
	f.close()




"""
Entree : liste de [id sequence, sequence], nom fichier sortie
Sortie : fichier fasta
"""
def WriteFasta2(liste, file_out):
	f = open(file_out, 'w')
	
	for seq in range(len(liste)) :
		f.write(">"+liste[seq][0]+"\n")
		
		taille = len(liste[seq][1])

		if taille > 80 :
			for j in range(0, taille, 80):
				if j+80 > taille :
					f.write(liste[seq][1][j:taille])
			
				else :
					f.write(liste[seq][1][j:j+80])
			
				f.write("\n")
			
		else :
			f.write(liste[seq][1]+"\n")
		
	f.close()




"""
Entree : dictionnaire (clé : id, valeur : sequence), nom fichier sortie
Sortie : fichier fasta
"""
def WriteFasta3(dico, file_out):
	f = open(file_out, 'w')
	
	for seq in dico :
		f.write(">"+seq+"\n")
		
		taille = len(dico[seq])

		if taille > 80 :
			for j in range(0, taille, 80):
				if j+80 > taille :
					f.write(dico[seq][j:taille])
			
				else :
					f.write(dico[seq][j:j+80])
			
				f.write("\n")
			
		else :
			f.write(dico[seq]+"\n")
		
	f.close()
