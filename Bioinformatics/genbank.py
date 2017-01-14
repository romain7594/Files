# Retourne la séquence d'un genbank
def sequence(fichier):
	Sequence = ''

	F = open(fichier, 'r')
	ligne = F.readline()
	
	while not re.search("^SQ", ligne):
		ligne = F.readline()
	
	ligne = F.readline()
	
	while ligne[0] != '/':
		tmp = ligne[:-1].split()

		Sequence = Sequence+"".join(tmp[:-1])

		ligne = F.readline()
	
	F.close()
	Sequence = Sequence.upper()

	return Sequence
