##### 1 #####
def produit(a, b, c, d, e):
	return a*b*c*d*e
	
	
##### 2 #####
L = [1, 5.1, 65, 4.98, 1234, 98.7]

def supp_reels(liste):
	tmp = []
	
	for i in liste :
		if "." not in str(i) :
			tmp.append(i)
	
	return tmp


##### 3 #####
def func():
	x = ""
	L = []
	alphabet = ['abcdefghijklmnopqrstuvwxyz']
	
	x = raw_input("Entrez une variable : ")
	
	while x != -1 :
		if x != "-1" :
			caractere = False

			for i in x :
				if i in alphabet :
					caractere = True
					break

			if caractere :
				L.append(x)
			else :
				if "." in x :
					L.append(float(x))
				else :
					L.append(int(x))

			x = raw_input("Entrez une variable : ")
		
		else :
			x = -1
	
	return L


##### 4 #####
F = lambda x,y : x if x>y ; else y
