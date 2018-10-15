##### dia 75 #####
liste1 = [0, 45, 16, 78, 100, 65557687]
liste2 = [1.46, 1.987, 0.89787667]
liste3 = ['sldfjslkj', 'HGJK', 'P']
liste4 = [197979, 1.0980, 'lkjUYT']
liste5 = [liste1, liste3]

print liste1
print liste2
print liste3
print liste4
print liste5


##### dia 79 #####
truc = [1, 'lkfjxlkfjklf', 'POPO', 1.98]

print truc[0]
print truc[1]
print truc[3]
print truc[-1]


##### dia 81 #####
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print nombres
print nombres[0:5]
print nombres[3:6


##### dia 83 #####
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print liste
print liste[:]
print liste[:3]
print liste[3:]


##### dia 86 #####
UneListeVide = []
UneListePasVide = ['Ceci', 'est', 'une']

print UneListeVide
print UneListePasVide

UneListeVide.append('Bonjour')
UnelistePasVide.append('liste')

print UneListeVide
print UneListePasVide


##### dia 88 #####
nombres = [0, 1, 2, 4, 5]
prahse = ['Je', 'une', 'phrase']

print nombres
print phrase

nombres.insert(3, 3)
phrase.insert(1, 'contient')

print nombres
print phrase


##### dia 90 #####
nombres = [0, 1, 2, 47, 3, 4]
phrase = ['Je', 'ne', 'possede', 'pas', 'une', 'phrase']
exemple = ['coucou', 'bonjour', 'salut', 'wesh']

print nombres
print phrase
print exemple

nombres.remove(47)
phrase.remove('ne')
phrase.remove('pas')
exemple.remove(exemple[2])

print nombres
print phrase
print exemple


##### dia 92 #####
UnePhrase = ['Je', 'suis', 'en', 'train', 'de', 'coder', 'dormir']

print UnePhrase

mot = UnePhrase.pop()

print UnePhrase
print mot

liste = [1, 13, 16, 10, 20]

p = liste.pop(2)
print liste
print p

p = liste.pop(-1) #equivaut a liste.pop()
print liste
print p


##### dia 94 #####
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print nombre.index(4)
print nombre.index(nombre[4])
print nombre.index(9)


##### dia 97 #####
liste1 = ['Je', 'suis', 'en', 'train']
liste2 = ['de', 'taper', 'au clavier']
liste3 = [36, 12, 6]

print liste1
print liste2

liste4 = liste1+liste2

print liste4

#liste1.extend(liste2)
#print liste1


##### dia 98 #####
liste1 = ['Je', 'suis', 'en', 'train']
liste2 = ['de', 'taper', 'au clavier']
liste3 = [36, 12, 6]

liste5 = liste3*2

print liste5


##### dia 100 #####
nombres = [1, 2, 3, 4, 5, 6]

Vrai = 1 in nombres

print 0 in nombres
print Vrai


##### dia 102 #####
liste4 = ['Je', 'suis', 'en', 'train', 'de', 'taper', 'au', 'clavier']

phrase = " ".join(liste4)
phrase1 = "@".join(liste4)
phrase2 = "_".join(liste4)

print liste4
print phrase
print phrase1
print phrase2


##### dia 104 #####
UnePhrase = 'Ceci-est-une-phrase"

phrase = UnePhrase.split("-")

print UnePhrase
print phrase


##### dia 106 #####
liste2D = [[1, 2],[3, 4]]
liste3D = [[[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[10, 11, 12]]]
liste4D = [[[[1, 2],[3, 4]],[[5, 6],[7, 8]]],[[[9, 10],[11, 12]],[[13, 14],[15, 16]]]]

print liste1D
print liste2D[0]
print liste2D[0][1]

print liste3D
print liste3D[0]
print liste3D[0][1]
print liste3D[0][1][0]

print liste4D
print liste4D[0]
print liste4D[0][1]
print liste4D[0][1][0][1]


##### dia 109 #####
UnTuple = (12, 8.98, 'slfdkj', 'KLHJ87')
UnTuple2 = ((1, 2), (3, 4))

print UnTuple
print UnTuple[1]

print UnTuple2
print UnTuple2[0]
print UnTuple2[0][1]

UnTuple.remove(12)
