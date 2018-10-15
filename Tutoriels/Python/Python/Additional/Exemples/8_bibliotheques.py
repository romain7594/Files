##### dia 218 #####
# Note : pour voir l'effet des differents imports, ne lancez qu'un seul type d'import à la fois, mettre les autres en commentaire #

#
import 8_bibliotheques_fonctions
print 8_bibliotheques_fonctions.CARRE(2)

#
import 8_bibliotheques_fonctions as fn
print fn.CARRE(2)

#
from import 8_bibliotheques_fonctions import CARRE
print CARRE(2)

#
from import 8_bibliotheques_fonctions import *
print CARRE(2)
print CUBE(2)


##### dia 220 #####
print 'Bonjour'
print 'Voici'
print 'un exemple'

import 8_bibliotheques_fonctions

print 8_bibliotheques_fonctions.CARRE(2)

#
print 8_bibliotheques_fonctions.CARRE(2)

import 8_bibliotheques_fonctions
