import re

motif = re.compile("^\w{5}\s\w{2}\s\d\d\.\d\d\.\d\s[a-z]*\s[a-z]*\.\d\d\s(\w*)$")

c = "START NB 12.56.7 silhouette marche.49 fin"

r = motif.search(c)

print r.group(0)
print r.groupe(1)

print "Debut :", r.start()
print "Fin" :", r.end()
