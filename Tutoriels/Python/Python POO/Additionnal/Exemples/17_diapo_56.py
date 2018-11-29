class Exemple(object):
	def __init__(self, element):
		self.element = element
	
	def __and__(self, ex):
		return [self.element, ex.element]
		
E1 = Exemple("balle")
E2 = Exemple("ballon")
print(E1 & E2)
