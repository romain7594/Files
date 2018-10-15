##### dia 47 #####
import re

motif = re.compile('\s(\d*)\s.*\s(\d*)')

resultat = motif.search("J'ai eu 15 et toi 17")

print resultat.group(0)
print resultat.group(1)
print resultat.group(2)
print resultat.start()
print resultat.end()
