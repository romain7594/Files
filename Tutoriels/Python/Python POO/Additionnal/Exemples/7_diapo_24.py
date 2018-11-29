class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def retourne(self):
		return "La fonction retourne {} et {}".format(self.x, self.y)
		
P = Point(5, 6)
print(P.retourne())
