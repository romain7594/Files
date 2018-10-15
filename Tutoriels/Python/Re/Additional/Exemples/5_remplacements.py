##### dia 51 #####
import re

motif = re.compile('\d\d')

print motif.sub("6", "J'ai eu 15 et toi 17")
print motif.sub("6", "J'ai eu 15 et toi 17", count=1)
