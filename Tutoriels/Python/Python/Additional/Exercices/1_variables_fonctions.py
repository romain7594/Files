##### 1 #####
chaine = raw_input("Entrez une chaine de caracteres : ")

print type(chaine)
print len(chaine)

f = open("texte.txt", "w")

for i in range(5) :
	if i == 4 :
		f.write(chaine)
	else :
		f.write(chaine+"\n")
		
f.close()


##### 2 #####
nombre1 = 135649872545132168756465761231684.54654216548
nombre2 = 135649872545132168756495761231684.54654316548

if nombre1 > nombre2 :
	print "nombre1 est le plus grand"
else :
	print "nombre2 est le plus grand"
	
print "Difference :", str(abs(nombre1-nombre2))
