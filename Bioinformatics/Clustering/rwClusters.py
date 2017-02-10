#!/usr/bin/python
#-*- coding: utf-8 -*-

# Fonction qui ecrit les clusters dans un fichier
"""
Entree : liste des clusters, nom fichier sortie 
Sortie : fichier txt
"""
def writeClusters(groupes, output):
        f = open(output, 'w')
        f.write(str(len(groupes))+"\n\n")
        i = 1

        for C in groupes :
                f.write("Cluster "+str(i)+"\n")
                i += 1

                for element in C :
                        f.write(element+"\n")
                
                if element != groupes[-1][-1] :
                        f.write("\n")

        f.close()




# Fonction qui lit un fichier de clusters
"""
Entree : fichier cluster
Sortie : nombre de clusters, liste des clusters
"""
def readClusters(fichier) :
        f = open(fichier, "r")
        
        N = int(f.readline()[:-1])
        C = []

        L = f.readline()
        L = f.readline()
        
        while L != "" :
                if L.startswith("Cluster") :
                        C.append([])
                
                else :
                        if L[:-1] != '' :
                                C[-1].append(L[:-1])
                
                L = f.readline()
        
        return N, C
