class Point(object):
	forme = "rond"
	
	def __init__(self, x):
		self.x = x
		
P = Point(2)
print(P.forme)
P.forme = "carre"
print(P.forme)
