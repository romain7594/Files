class Panier(object):
	def __init__(self):
		self.nb_pommes = 4
		self.nb_bananes = 6
		
	def __add__(self, val):
		pp = Panier()
		PP.nb_pommes += val[0]
		PP.nb_bananes += val[1]
		return PP
		
	def __str__(self):
		return "pommes : {}\nbananes : {}".format(self.nb_pommes, self.nb_bananes)
		
P = Panier()
P2 = P+[30, 17]
print(P2)
