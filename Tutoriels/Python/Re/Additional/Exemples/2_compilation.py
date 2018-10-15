##### dia 44 #####
import re

motif = re.compile("^Bonjour")

print motif

chaine = "Bonjour toi"

print motif.search(chaine)

chaine2 = "Hey toi ! Bonjour !"

print motif.search(chaine2)
