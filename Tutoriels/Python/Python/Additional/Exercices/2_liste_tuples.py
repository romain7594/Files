##### 1 #####
L = range(17)

for i in [2, 4, 6, 10, 15] :
	L.remove(i)
	
print L


##### 2 #####
L = [5, 6, 4, 98, -3, 51, -46, -7, 52]
L = sorted(L, reverse=True)

print L


##### 3 #####
chaine = "Affectez cette chaine de caractères dans une variable puis mettre chaque mot de cette chaine dans une liste"
chaine = chaine.split(" ")

print chaine


##### 4 #####
chaine = "Affectez cette chaine de caractères dans une variable puis mettre chaque mot de cette chaine dans une liste"
chaine = chaine.split(" ")

new_chaine = "*".join(chaine)

print new_chaine


##### 5 #####
chaine = "Affectez cette chaine de caractères dans une variable puis mettre chaque mot de cette chaine dans une liste"
chaine = chaine.split(" ")

print chaine

chaine = []

print chaine


##### 6 #####
L1 = ['bonjour', 'salut', 'wesh']
L2 = [1, 2, 3]
L3 = []

L3.append(L1)
L3.append(L2)

print L3


##### 7 #####
print L3[0][2]
print L3[1][1]
