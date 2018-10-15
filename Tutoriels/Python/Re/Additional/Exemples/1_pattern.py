##### dia 42 #####
import re

chaine = "salut wesh bonjour coucou"

print re.search('wesh', chaine)
print re.search('hi', chaine)

if re.search('hello', chaine):
	print "C'est dedans"

else:
	print "C'est pas dedans"
