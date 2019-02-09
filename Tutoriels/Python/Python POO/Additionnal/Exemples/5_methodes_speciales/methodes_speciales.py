##### dia 43 #####
class Point(object):
        def __init__(self, x, y):
                self.x = x
                self.y = y


P = Point(1, 2)
print(P)


###################################################


class Point(object):
        def __init__(self, x, y):
                self.x = x
                self.y = y

        def __str__(self):
                return "x : {}, y : {}".format(self.x, self.y)


P = Point(1, 2)
print(P)
print(str(P))


##### dia 44 #####
class Point(object):
        def __init__(self, x, y):
                self.x = x
                self.y = y

        def __repr__(self):
                return "y : {}, x : {}".format(self.y, self.x)


P = Point(1, 2)
print(P)
print(repr(P))


##### dia 46 #####
class Panier(object):
        def __init__(self):
                self.nb_pommes = 4
                self.nb_bananes = 6

        def __add__(self, val):
                PP = Panier()
                PP.nb_pommes += val[0]
                PP.nb_bananes += val[1]
                return PP

        def __str__(self):
                return "pommes : {}\nbananes : {}".format(self.nb_pommes, self.nb_bananes)


P = Panier()
P2 = P + [30, 17]
print(P2)


##### dia 48 #####
class Personne(object):
        def __init__(self, prenom, taille):
                self.prenom = prenom
                self.taille = taille

        def __lt__(self, P):
                if self.taille > P.taille:
                        return True
                else:
                        return False


P = Personne("Bernard", 170)
P2 = Personne("Gregoire", 176)

print(P < P2)


##### dia 49 #####
class Exemple(object):
        def __init__(self, element):
                self.element = element

        def __and__(self, ex):
                return [self.element, ex.element]


E1 = Exemple("balle")
E2 = Exemple("ballon")
print(E1 & E2)


##### dia 51 #####
class Exemple(object):
        def __init__(self, element):
                self.element = element

        def __getattr__(self, nom):
                return "L'attribut {} n'existe pas".format(nom)


E = Exemple("voiture")
print(E.elemen)


###################################################


class Exemple(object):
        def __init__(self, element):
                self.element = element

        def __getattr__(self, nom):
                return self.element


E = Exemple("voiture")
print(E.elemen)


##### dia 52 #####
class Exemple(object):
        def __setattr__(self, attr, val):
                self.attr = val


E = Exemple()
E.element = "voiture"


###################################################


class Exemple(object):
        def __setattr__(self, attr, val):
                print("L'attribut {} a bien ete cree".format(attr))
                return object.__setattr__(self, attr, val)


E = Exemple()
E.element = "voiture"


##### dia 53 #####
class Exemple(object):
        def __init__(self):
                self.objet = "Diamant"

        def __delattr__(self, attribut):
                raise AttributeError("Suppression impossible")


E = Exemple()
del E.objet


##### dia 54 #####
class Exemple(object):
        def __init__(self):
                self.objet = "Diamant"

        def __setattr__(self, attribut, valeur):
                raise AttributeError("Modification impossible")


E = Exemple()
E.objet = "Je vous l'emprunte"


##### dia 56 #####
class Exemple(object):
        def __init__(self):
                self.objet = [1, 2, 3, 4, 5]

        def __getitem__(self, indice):
                return self.objet[indice]

        def __setitem__(self, indice, valeur):
                self.objet[indice] = valeur


E = Exemple()
print(E[0])
E[0] = 0
print(E[0])
