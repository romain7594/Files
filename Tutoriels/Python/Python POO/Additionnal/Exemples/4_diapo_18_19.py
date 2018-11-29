class Point(object):
	def __init__(self):
		self.x = 1
		self.y = 3
		
P = Point()
x, y = P.x, P.y

print("x : {}, y : {}".format(x, y))
#print(Point().x)
