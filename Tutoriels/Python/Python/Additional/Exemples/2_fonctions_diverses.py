##### dia 35 #####
numero1 = 1
mot = 'Bonjour'

print numero1
print mot
print 'Turlututu'
print '3690

print numero1, mot, 9789687, 'dsfkljdslkfj'


##### dia 37 #####
untruc = raw_input()
n = input("Un nombre : ")
lettre = raw_input("Une lettre : ")
phrase = raw_input("Une phrase : ")

print untruc
print n
print lettre
print phrase


##### dia 39 #####
type_int = 14
type_float = 1.2
type_str = 'coucou'
unknown_type = type(1868768681)

print type(type_int)
print type(type_float)
print type(type_str)
print type(unknown_type)


##### dia 41 #####
nombre = 76
caractères = 890

print nombre
print type(nombre)
print caracteres
print type(caracteres)

nombre = float(nombre)
caracteres = str(caracteres)

print nombre
print type(nombre)
print caracteres
print type(caracteres)


##### dia 43 #####
mot = 'bonjour'
UnChaine = 'slfkjkldfgdfxgjdfnk87hbkn546bkn879Vbkjb767'

print len(mot)
print len(UneChaine)


##### dia 45 #####
VingtElements = range(20)
DebutFin = range(10, 20)
AvecUnPasPositif = range(0, 10, 2)
AvecUnPasNegatif = range(10, 0, -1)

print range(10)
print DebutFin
print VingtElements
print AvecUnPasPositif
print AvecUnPasNegatif


##### dia 47 #####
mot = abcdef
nombres = range(10)

print mot
print nombres

print reversed(mot)
print reversed(nombres)

print type(reversed(mot))
print type(reversed(nombres))


##### dia 54 #####
fichier = open('2_fonctions_diverses_texte_dia_54.txt', 'r')

ligne = fichier.readline()

print type(ligne)
print ligne

fichier.close()


##### dia 57 #####
fichier = open('2_fonctions_diverses_texte_dia_54.txt', 'r')

ligne = fichier.readline()
print ligne
ligne = fichier.readline()
print ligne
ligne = fichier.readline()
print ligne
ligne = fichier.readline()
print ligne

fichier.close()


##### dia 59 #####
fichier = open('2_fonctions_diverses_texte_dia_54.txt', 'r')

lignes = fichier.readlines()

print lignes

fichier.close()


##### dia 61 #####
fichier = open('texte2.txt', 'w')

fichier.write("Ceci est une chaine de caracteres")

fichier.close()


##### dia 63 #####
fichier = open('2_fonctions_diverses_texte_dia_54.txt', 'a')

fichier.write('cinquieme ligne')

fichier.close()


##### dia 65 #####
nombre1 = 3
nombre2 = 76
nombre3 = 40
nombre4 = max(nombre2, nombre3)
nombre5 = min(nombre2, nombre3)

print nombre4
print max(nombre1, nombre3)
print max(nombre1, nombre2, nombre3)

print nombre5
print min(nombre1, nombre2, nombre3)
print min(nombre2, nombre3)


##### dia 67 #####
nombres = range(10, 0, -1)
lettres = 'dkfhskfhksjh'

print nombres
print sorted(nombres)
print sorted(lettres)

nombres = range(10)
lettres = 'kjqshlskvfdkljm'

print nombres
print sorted(nombres, reverse=True)
print sorted(lettres, reverse=True)

               
