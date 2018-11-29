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
