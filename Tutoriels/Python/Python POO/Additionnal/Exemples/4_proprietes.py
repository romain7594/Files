##### dia 31 #####
class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

P = Point(0, 1)
print("x : {}, y : {}".format(P.x, P.y))

P.x = 14
P.y = 6
print("x : {}, y : {}".format(P.x, P.y))


##### dia 34 et 36 #####
class Point(object):
	def __init__(self, x, y):
		self._x = x
		self._y = y
		
	def _get_x(self):
		return self._x
		
	def _set_x(self, valeur):
		self._x = valeur
		
	x = property(_get_x, _set_x)
	
P = Point(0, 0)
P.x = 2

print("x : {}".format(P.x))
