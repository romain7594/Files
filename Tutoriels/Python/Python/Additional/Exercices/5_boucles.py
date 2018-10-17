##### 1 #####
nb_max = 30
nb_personnes = 2
t = 0

while nb_personnes < nb_max :
	t += 5
	nb_personnes += 2

print "Temps :", t, "min"


##### 2 #####
somme = input("Entrez un nombre entier : ")
i = 1

while somme <= 100 :
	tmp = input("Entrez un nombre entier : ")
	somme += tmp
	i += 1

print str(somme)+" a été obtenu en additionnant "+str(i)" nombres"
