class Point(object):
	def _init__(self, x, y):
		self.x = x
		self.y = y

P = Point(1, 2)
print(P)

###################################################

class Point(object):
	def _init__(self, x, y):
		self.x = x
		self.y = y
	
	def __str__(self):
		return "x : {}, y : {}".format(self.x, self.y)
		
P = Point(1, 2)
print(P)
print(str(P))
