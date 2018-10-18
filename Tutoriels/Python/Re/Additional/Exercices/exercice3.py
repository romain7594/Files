import re

L = []
D = {}

nom_famille = re.compile("\s(\w*)$")
numero = re.compile("^(\d{1,4})\s")
nom_rue = re.compile("\d{1,4}\s(\.*)$")
code_postal = re.compile("^(\d{5})\s")
ville = re.compile("^\d{5}\s(\.*)$")

f = open("adresse.txt", 'r')

line = f.readline()

while line != "" :
	if line == "\n" :
		L.append(D)
		D = {}
	
	else :
		S = nom_famille.search(line)
		if S :
			D["nom famille"] = S.group(1)
			
		S1 = numero.search(line)
		if S1 :
			D["numero"] = S1.group(1)
			
		S2 = nom_rue.search(line)
		if S2 :
			D["nom rue"] = S2.group(1)
			
		S3 = code_postal.search(line)
		if S3 :
			D["code postal"] = S3.group(1)
			
		S4 = ville.search(line)
		if S4 :
			D[ville"] = s4.group(1)
		
	line = f.readline()

f.close()

L.append(D)

for personne in L :
	print "Nom :", personne["nom famille"]
	print "Adresse :", personne["numero"], personne["nom rue"]
	print "Ville :", personne["code postal"], personne["ville"], "\n"
		
