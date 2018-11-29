class Personne(object):
	def __init__(self, prenom, taille):
		self.prenom = prenom
		self.taille = taille
		
	def __lt__(self, P):
		if self.taille > P.taille :
			return True
		else :
			return False
			
P = Personne("Bernard", 170)
P2 = Personne("Gregoire", 176)

print(P < P2)
