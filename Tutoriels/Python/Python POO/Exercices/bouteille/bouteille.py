class Cylindre(object):
	def __init__(self, hauteur, rayon):
                self.hauteur = hauteur
                self.rayon = rayon

        def volume(self, h):
                V = 3.14*(self.rayon**2)*h
                return V


class ActionRecipient(object):
        pass


class Bouteille(Cylindre, ActionRecipient):
        def __init__(self, hauteur, rayon):
                Cylindre.__init__(self, hauteur-hauteur//4, rayon)
                self.hauteur_cone = hauteur//4

        def volume(self):
                V = super(Bouteille, self).volume(self.hauteur)
                C = super(Bouteille, self).volume(self.hauteur_cone)/3
                return C+V
