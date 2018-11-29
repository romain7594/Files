class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

P = Point(0, 1)
print("x : {}, y : {}".format(P.x, P.y))

P.x = 14
P.y = 6
print("x : {}, y : {}".format(P.x, P.y))
