class Cylindre(object):
        def __init__(self, hauteur, rayon):
                self.hauteur = hauteur
                self.rayon = rayon

        def volume(self, h):
                V = 3.14*(self.rayon**2)*h
                return V


class ActionRecipient(object):
        def remplir(self, r):
                if self.quantite == self.quantite_max :
                        print("La bouteille est pleine")
                else :
                        if self.quantite+r > self.quantite_max :
                                self.quantite = self.quantite_max
                        else :
                                self.quantite += r

        def vider(self, v):
                if self.quantite == 0 :
                        print("La bouteille est vide")
                else :
                        if v <= self.quantite :
                                self.quantite -= v
                        elif v > self.quantite :
                                self.quantite = 0


class Bouteille(Cylindre, ActionRecipient):
        def __init__(self, hauteur, rayon, quantite=0):
                Cylindre.__init__(self, hauteur-hauteur//4, rayon)
                self.hauteur_cone = hauteur//4
                self.quantite = quantite
                self.quantite_max = 100

        def volume(self):
                V = super().volume(self.hauteur)
                C = super().volume(self.hauteur_cone)/3
                return C+V

        def __str__(self):
                return "La bouteille contient {} unite(s) de liquide".format(self.quantite)

T = Bouteille(6, 3, 50)
T.remplir(60)
print(T)
T.remplir(10) # Bouteille pleine
T.vider(80)
print(T)
T.vider(30) # Bouteille vide
print(T)
T.vider(50)
