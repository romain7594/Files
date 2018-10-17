#!/usr/bin/python
#-*- coding: utf-8 -*-

import math
import random                                  ######## ajout de import random

variable1 = 100                                ######## pas d'accent dans un nom de variable
variable2 = 500                                ######## indentation non nécessaire
variable3 = 13.8                               ######## indentation non nécessaire
	
print math.log(variable1, 10)

for i in range(20):                            #######  ":" à la fin d'un for
	variable1 = variable+10
	
	if variable1 == 200:
		print "Supérieur à 200"         ####### indentation
	
	
if variable2 > 300:
	print "Oh bien !!!"                     ####### " à la place de ' avant Oh
	variable3 = variable2+variable3

else:
	print "Peut mieux faire"
	
valeur_aleatoire = random.random()             ####### import random au début, ou avant cette ligne
print valeur_aleatoire

print "Vous avez reussi !!!!"                  ####### Oublié d'un " au début de la chaine
