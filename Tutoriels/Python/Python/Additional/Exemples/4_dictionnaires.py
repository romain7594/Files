##### dia 117 #####
Age = {'Bernard' : 18, 'Michel' : 20, 'Lucie' : 23, 'Martine' : 21}

print Age['Bernard']
print Age['Michel']
print Age['Lucie']
print Age['Martine']


##### dia 119 #####
capitale = {'France' : 'Paris', 'Angleterre' : 'Londres', 'Espagne' : 'Madrid'}

print capitale

capitale['Italie'] = 'Rome'

print capitale
print capitale['Italie']


##### dia 121 #####
capitale = {'France' : 'Paris', 'Angleterre' : 'Londres', 'Espagne' : 'Madrid'}

print capitale

capitale['Italie'] = ''

print capitale
print capitale['Italie']

capitale['Italie'] = 'UneVille'

print capitale
print capitale['Italie']

capitale['Italie'] = 'Rome'

print capitale
print capitale['Italie']


##### dia 123 #####
capitale = {'France' : 'Paris', 'Angleterre' : 'Londres', 'Espagne' : 'Madrid'}

print capitale

capitale['Italie'] = 'Rome'

print capitale

del capitale['Italie']

print capitale


##### dia 125 #####
capitale = {'France' : 'Paris', 'Angleterre' : 'Londres', 'Espagne' : 'Madrid'}

print capitale

capitale.clear()
#capitale = {}

print capitale


##### dia 128 #####
Maison = {'Salon' : 1, 'Chambre' : 2, 'Salle de bain' : 2, 'Cuisine' : 1}

Pieces = Maison.keys()
NombrePieces = Maison.values()
LesDeux = Maison.items()

print Pieces
print NombrePieces
print LesDeux


##### dia 130 #####
Maison = {'Salon' : 1, 'Chambre' : 2, 'Salle de bain' : 2, 'Cuisine' : 1}

print Maison.kas_key('Salon')
print Maison.has_key('Garage')


##### dia 131 #####
capitale = {'France' : 'Paris', 'Angleterre' : 'Londres', 'Espagne' : 'Madrid'}

print 'France' in capitale
print 'Italie' in capitale
