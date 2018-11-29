class Exemple(object):
	def __init__(self):
		self.objet = "Diamant"
		
	def __setattr__(self, attribut, valeur):
		raise AttributeError("Modification impossible")
		
E = Exemple()
E.objet = "Je vous l'emprunte"
