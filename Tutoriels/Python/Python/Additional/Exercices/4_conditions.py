##### 1 #####
a = input("Entrez un premier nombre : ")
b = input("Entrez un deuxième nombre : ")
c = input("Entrez un toisième nombre : ")

if a+b+c > 100 :
	print "OK"
else :
	print "PAS OK"


##### 2 #####
notes = {'maths' : 10, 'histoire' : 12, 'français' : 14, 'langues' : 11, 'biologie' : 5, 'physique chimie' : 2}

if sum(notes.values()) >= 10 :
	print "Tu passes"
elif (sum(notes.values()) > 8) and (sum(notes.values()) <= 10) :
	print "Seconde chance accordée"
else :
	print "Recalé"


##### 3 #####
classe = ['Maxime', 'Benjamin', 'Pierre', Marianne', 'Manon', 'Denis']

if len(classe) == 7 :
	print "Le cours commence"
else :
	print "On attend"
	
classe.append("Toto")

if len(classe) == 7 :
	print "Le cours commence"
else :
	print "On attend"
