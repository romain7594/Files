##### dia 72 #####
class A(object):
        pass

class B(A):
        pass


##### dia 73 #####
class A(object):
        def __init__(self):
                self.a = 1
                self.b = 2

        def affiche(self):
                print(self.a, self.b)

class B(A):
        pass

P = B()
print(P.a, P.b)
P.affiche()


##### dia 74 et 75 #####
class Cylindre(object):
        def __init__(self, hauteur, rayon):
                self.hauteur = hauteur
                self.rayon = rayon

        def aire(self):
                A = 2 * 3.14 * self.rayon * self.hauteur + 2 * 3.14 * (self.rayon ** 2)
                return A

        def volume(self):
                V = 3.14 * (self.rayon ** 2) * self.hauteur
                return V

class Bouteille(Cylindre):
        def __init__(self, hauteur, rayon):
                self.hauteur = hauteur
                self.rayon = rayon


##### dia 77 #####
class UnObjet(object):
        def affiche(self):
                print("Hello")

class UnTruc(UnObjet):
        def affiche(self):
                print("Bonjour")

class UneChose(UnObjet):
        pass

A = UnObjet()
B = UnTruc()
C = UneChose()

A.affiche()
B.affiche()
C.affiche()


##### dia 78 #####
class Bouteille(Cylindre):
        def __init__(self, hauteur, rayon):
                Cylindre.__init__(self, hauteur, rayon)

T = Bouteille(6, 4)

print(T.rayon)
print(T.hauteur)


##### dia 79 #####
class Bouteille(Cylindre):
        def __init__(self, hauteur, rayon):
                Cylindre.__init__(self, hauteur, rayon)
                self.matiere = "plastique"
                self.contenu = "eau gazeuse"

class RouleauDePapierToilette(Cylindre):
        def __init__(self, hauteur, rayon):
                Cylindre.__init__(self, hauteur, rayon)
                self.poids = 200
                self.utilisation = "hygiene"

T = Bouteille(6, 4)
print("Bouteille en {} contenant de l'{}".format(T.matiere, T.contenu))

R = RouleauDePapierToilette(4, 2)
print("Rouleau de papier toilette pesant {}g et ayant une fonction d'{}".format(R.poids, R.utilisation))


##### dia 81 et 82 #####
class Cylindre(object):
        def __init__(self, hauteur, rayon):
                self.hauteur = hauteur
                self.rayon = rayon

        def volume(self, h):
                V = 3.14 * (self.rayon ** 2) * h
                return V

class Bouteille(Cylindre):
        def __init__(self, hauteur, rayon):
                Cylindre.__init__(self, hauteur - hauteur // 4, rayon)
                self.hauteur_cone = hauteur // 4

        def volume(self):
                V = super(Bouteille, self).volume(self.hauteur)
                C = super().volume(self.hauteur_cone) / 3
                return C + V

T = Bouteille(8, 2)
print(T.volume())
