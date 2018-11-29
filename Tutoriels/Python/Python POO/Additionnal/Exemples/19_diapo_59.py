class Exemple(object):
	def __setattr__(self, attr, val):
		self.attr = val
		
E = Exemple()
E.element= "voiture"


###################################################


class Exemple(object):
	def __setattr__(self, attr, val):
		print("L'attribut {} a bien ete cree".format(attr))
		return object.__setattr__(self, attr, val)
		
E = Exemple()
E.element= "voiture"
