##### dia 49 #####
import re

motif = re.compile('\d*\.\d*')

resultat = motif.findall("J'ai eu 15.6 et toi 17.9")

print resultat

motif = re.compile('(\d*)\.(\d*)')

resultat = motif.findall("J'ai eu 15.6 et toi 17.9")

print resultat
