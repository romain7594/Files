class Exemple(object):
	def __init__(self, element):
		self.element = element
		
	def __getattr__(self, nom):
		return "L'attribut {} n'existe pas".format(nom)
		
E = Exemple("voiture")
print(E.elemen)


#######################################


class Exemple(object):
	def __init__(self, element):
		self.element = element
		
	def __getattr__(self, nom):
		return self.element
		
E = Exemple("voiture")
print(E.elemen)
