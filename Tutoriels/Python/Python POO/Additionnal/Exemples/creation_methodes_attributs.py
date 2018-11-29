##### dia 12 #####

class NomDeLaClasse(object):
	pass


##### dia 18 et 19 #####
class Point(object):
	def __init__(self):
		self.x = 1
		self.y = 3
		
P = Point()
x, y = P.x, P.y

print("x : {}, y : {}".format(x, y))
#print(Point().x)


##### dia 21 #####
class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
class PointBis(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		
P = Point(6, 4)
Pbis1 = PointBis()
Pbis2 = PointBis(2, 3)

print("x : {}, y : {}".format(P.x, P.y))
print("x : {}, y : {}".format(Pbis1.x, Pbis1.y))
print("x : {}, y : {}".format(Pbis2.x, Pbis2.y))


##### dia 23 #####
class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def affiche(self):
		print("x : {}, y : {}".format(self.x, self.y))
		
P = Point(1, 2)
P.affiche()


##### dia 24 #####
class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def retourne(self):
		return "La fonction retourne {} et {}".format(self.x, self.y)
		
P = Point(5, 6)
print(P.retourne())
