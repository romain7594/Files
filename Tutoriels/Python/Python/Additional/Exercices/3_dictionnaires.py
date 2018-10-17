ordinateur = {'ecran' : 1, 'clavier' : 1, 'souris' : 1, 'unitecentrale' : 1}

##### 1 #####
if "enceinte" in ordinateur :
	print "Je possède des enceintes"
else :
	print "Je ne possède pas d'enceintes"

print "Je possède "+str(ordinateur["souris"])+" souris"


##### 2 #####
ordinateur["webcam"] = 1
ordinateur["enceintes"] = 2


##### 3 #####
del ordinateur["ecran"]
ordinateur["super ecran"] = 1


##### 4 #####
ordinateur.clear()
ordinateur = {'ecran tout en 1' : 1, 'clavier' : 1, 'souris' : 1}


##### 5 #####
print "Mon ordinateur est composé de "+len(ordinateur)+" éléments"
A = ordinateur.items()
C = ""

for i in A :
	C += str(i[1])+i[0]+", "
	
print "Il est composé de :", C[:-2]
