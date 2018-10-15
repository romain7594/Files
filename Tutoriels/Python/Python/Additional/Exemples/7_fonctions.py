##### dia 183 #####
def multiplie_par_deux(nombre):

	nombre2 = nombre*2
	
	return nombre2
	
print multiplie_par_deux(4)


##### dia 185 #####
def affiche(nombre):
	print nombre
	print nombre
	print nombre
	print nombre
	print nombre
	print nombre

affiche(4)


##### dia 186 #####
def return_None() :
	return
	
print return_None()


##### dia 188 #####
def UneFonction():
	print "Un truc"
	print "Un autre truc"
	
	return "Un dernier truc"

UneFonction()
print UneFonction()


##### dia 190 et 191 #####
def fonction(nombre):
	if nombre == 1 :
		return "On s'arrête ici"
	
	else :
		return "On s'arrête là"
		
	print "OleyOleyOley"
	
	return "Pourquoi pas ici ?"

print fonction(1)
print fonction(98765)


##### dia 193 #####
def met_au_carre(x):
	
	p = x*x
	
	return p

nombre = 2

print met_au_carre(nombre)


##### dia 196 #####
def affiche_les_arguments(x, y, z):
	print x
	print y
	print z
	
	return x, y, z
	
nombre1 = 1
nombre2 = 2
nombre3 = 3

N = affiche_les_arguments(nombre1, nombre2, nombre3)


##### dia 199 #####
def affiche_les_arguments(x, y, z):
	print x
	print y
	print z
	
	return x, y, z
	
nombre1 = 1
nombre2 = 2
nombre3 = 3

N = affiche_les_arguments(nombre1, nombre2, nombre3)

print type(N)
print N

N1, N2, N3 = affiche_les_arguments(nombre1, nombre2, nombre3)

print N1
print N2
print N3


##### dia 201 #####
def met_au_carre(nombre):
	
	return nombre*nombre


def appelle_la_fonction_avant(nombre):
	
	resultat = met_au_carre(nombre)
	
	return resultat
	
print appelle_la_fonction_avant(4)


##### dia 202 #####
print appelle_la_fonction_avant(4)


def met_au_carre(nombre):
	
	return nombre*nombre
	
	
def appelle_la_fonction_avant(nombre):
	
	resultat = met_au_carre(nombre)
	
	return resultat


##### dia 204 #####
def appelle_la_fonction_avant(nombre):
	
	resultat = met_au_carre(nombre)
	
	return resultat
	
	
def met_au_carre(nombre):
	
	return nombre*nombre
	
	
print appelle_la_fonction_avant(4)


##### dia 206 #####
fois_deux = lambda x : x*2

#def fois_deux(x) :
	#return x*2
	
print fois_deux(4)

add = lambda x,y : x+y

#def add(x,y):
	#return x+y

print add(3,8)
