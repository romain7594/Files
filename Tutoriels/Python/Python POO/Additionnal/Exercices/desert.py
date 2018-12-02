import random

argent = random.randint(0, 150)

class Voiture(object):
        def __init__(self):
                self.essence = 0
                self.demarre = False

        def fill(self, valeur):
                self.essence += valeur/2.3

        def start(self):
                if self.essence > 0 :
                        self.demarre = True
                        print("Vroum !")
                else :
                        print("Tonerre de Brest !")

        def ride(self):
                if self.demarre :
                        if self.essence >= 48 :
                                print("Super !")
                        else :
                                print("Mille millions de mille sabords !!!")
                                print("Vous ne pouvez que parcourir {} km".format(round(self.essence/1.6, 1)))

                else :
                        raise Exception("Vous devez demarrer la voiture")

V = Voiture()
V.fill(argent)
V.start()
V.ride()
