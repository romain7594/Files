##### dia 225 #####
import math

racine_carre = math.sqrt(9)
logarithme = math.log(0.87687)
exponentielle = math.exp(1)
cosinus = math.cos(math.pi)

print racine_carre
print logarithme
print exponentielle
print cosinus


##### dia 227 #####
import random

liste = ['untruc', 87687, 1.9]

entier_aleatoire = random.randint(10, 20)
entre_zero_et_un = random.random()
reel_aleatoire = random.uniform(0, 30)
dans_une_liste = random.choice(liste)

print entier_aleatoire
print entre_zero_et_un
print reel_aleatoire
print dans_une_liste


##### dia 229 et 231 #####
import copy

liste = [1, 2, 3, 4, 5]
liste2 = liste
#liste2 = copy.copy(liste)

print liste
print liste2

liste[0] = 0

print liste
print liste2


##### dia 232 #####
import numpy

matrice = numpy.array([[1, 2], [3, 4]])

liste = [[5, 6], [7, 8]]

print matrice
print liste
print numpy.array(liste)

zeros = numpy.zeros((2, 3))
uns = numpy.ones((4, 2))


##### dia 234 #####
import numpy

matrice = numpy.array([[1, 2], [3, 4]])

print matrice

matrice[0][0] = 387686

print matrice

matrice[0][0] = 'unMot'


##### dia 235 #####
import matplotlib.pyplot

liste_des_x = [0, 1, 2, 3, 4]
liste_des_y = [76, 98, 5, 34, 10]

matplotlib.pyplot.plot(liste_des_x, liste_des_y)
matplotlib.pyplot.xlabel('Axe des x')
matplotlib.pyplot.ylabel('Axe des y')
matplotlib.pyplot.show()
