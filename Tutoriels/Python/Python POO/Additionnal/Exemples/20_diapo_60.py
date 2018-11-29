class Exemple(object):
	def __init__(self):
		self.objet = "Diamant"
		
	def __delattr__(self, attribut):
		raise AttributeError("Suppression impossible")
		
E = Exemple()
del E.objet
