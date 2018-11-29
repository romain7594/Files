class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __repr__(self):
		return "y : {}, x : {}".format(self.y, self.x)

P = point(1, 2)
print(P)
print(repr(P))
