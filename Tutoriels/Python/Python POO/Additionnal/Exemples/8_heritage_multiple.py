##### dia 86 #####
class ClasseMere(object):
	def affiche1(self):
		print("Je suis ta mere")
		
class ClassePere(object):
	def affiche2(self):
		print("Je suis ton pere")
		
class ClasseFille(ClasseMere, ClassePere):
	pass
	
F = ClasseFille()
F.affiche1()
F.affiche2()


##### dia 87 #####
class ClasseMere(object):
	def affiche(self):
		print("Je suis ta mere")
		
class ClassePere(object):
	def affiche(self):
		print("Je suis ton pere")
		
class ClasseFille(ClasseMere, ClassePere):  # class ClasseFille(ClassePere, ClasseMere):
	pass
	
F = ClasseFille()
F.affiche()
