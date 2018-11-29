##### dia 39 et 40 #####
class Point(object):
	forme = "rond"
	
	def __init__(self, x):
		self.x = x
		
P = Point(2)
print(P.forme)
P.forme = "carre"
print(P.forme)


##### dia 41 #####
class Point(object):
	forme = "rond"
	
	def __init__(self, x):
		self.x = x
		
P = Point(2)
print("avant modification de la forme de P :", P.forme)
P.forme = "carre"
print("apres modification de la forme de P :", P.forme)

P1 = Point(3)
print("forme de la classe Point non affecte pour un nouveau point :", P1.forme)

Point.forme = "carre"

P2 = Point(4)
print("apres modification de la forme de la classe Point :", P2.forme)
