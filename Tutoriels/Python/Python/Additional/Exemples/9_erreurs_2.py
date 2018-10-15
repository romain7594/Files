##### dia 267 #####
n = 12

try :
	a = n/0
	print a
except :
	print "il y a une erreur"


##### dia 269 #####
n = 12

try :
	a = n/8
	print a

except ZeroDivisionError :
	print "Bip ! Division par zero"

except NameError :
	print "Bip ! Variable inexistante"

except :
	print "il y a une erreur"


#
n = 12

try :
	print a
	a = n/8

except ZeroDivisionError :
	print "Bip ! Division par zero"

except NameError :
	print "Bip ! Variable inexistante"

except :
	print "il y a une erreur"



##### dia 270 #####
n = 12
l = [0, 1]

try :
	l[2] = 2
	print a
	a = n/8

except ZeroDivisionError :
	print "Bip ! Division par zero"

except NameError :
	print "Bip ! Variable inexistante"

#except :
	#print "il y a une erreur"


##### dia 272 #####
print 1

raise ZeroDivisionError("On ne divise pas par 0 !")

print 2


##### dia 273 #####
a = 1
b = 2

try :
	c = a+b
	if c < 4 :
		raise ValueError("le resultat est inferieur a 4 !")

except ValueError :
	print "a ou b est trop petit"
	
	
##### dia 275 #####
a = 1
b = 2

assert a == b

print "ici"


#
a = 1
b = 2
c = 4

try :
	d = a+b
	assert c == d
	print "OK"

except AssertionError : # ou juste except :
	print "ce n'est pas bon"
	

##### dia 276 #####
a = 1
b = 2
c = 4

try :
	d = a+b
	assert c == d
	print "OK"

except AssertionError : # ou juste except :
	pass

print "fin du programme"


##### dia 277 #####
def fonc(a,b):
	try :
		assert a == b
		print "OK"
	
	except :
		print "pas OK"
		return
	
	print "fin du programme"

fonc(1,2)


#
def fonc(a,b):
	try :
		assert a == b
		print "OK"
	
	except :
		print "pas OK"
		return
	
	finally :
		print "fin du programme"

fonc(1,2)
