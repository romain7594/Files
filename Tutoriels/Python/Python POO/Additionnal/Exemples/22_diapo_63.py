class Exemple(object):
	def __init__(self):
		self.objet = [1, 2, 3, 4, 5]
		
	def __getitem__(self, indice):
		return self.objet[indice]
	
	def __setitem__(self, indice, valeur):
		self.objet[indice] = valeur
		
E = Exemple()
print(E[0])
E[0] = 0
print(E[0])
