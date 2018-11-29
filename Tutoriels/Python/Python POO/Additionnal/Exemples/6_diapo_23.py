class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def affiche(self):
		print("x : {}, y : {}".format(self.x, self.y))
		
P = Point(1, 2)
P.affiche()
