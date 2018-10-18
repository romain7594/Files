import re

motif = re.compile("^\w{5}\s\w{2}\s\d\d\.\d\d\.\d\s[a-z]*\s[a-z]*\.\d\d\s\w*$")

c = "START NB 12.56.7 silhouette marche.49 fin"

print motif.search(c)
