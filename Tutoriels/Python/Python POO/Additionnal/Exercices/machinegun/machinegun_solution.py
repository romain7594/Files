import contextlib, random, sys
with contextlib.redirect_stdout(None):
        import pygame

import random, sys

pygame.mixer.init()

class MachineGun(object):
        def __init__(self):
                self._magazine = 50
                self._bullets = 200

        def _get_magazine(self):
                return self._magazine

        def _set_magazine(self, val):
                self._magazine = val

        magazine = property(_get_magazine, _set_magazine)

        def _get_bullets(self):
                return self._bullets

        def _set_bullets(self, val):
                self._bullets = val

        bullets = property(_get_bullets, _set_bullets)

        def fire(self):
                pygame.mixer.Sound("fire.wav").play()
                while pygame.mixer.get_busy():
                        pass

                self.magazine -= random.randint(1, 21)

                if self.magazine <= 0 :
                        self.magazine = 0
                        print("Bullets remaining : 0")
                else :
                        print("Bullets remaining : {}".format(self.magazine))

        def reload(self):
                if self.magazine == 50 :
                        print("Failed to reload. Magazine full")

                else :
                        if self.bullets > 0:
                                if self.bullets >= 50 :
                                        if self.magazine == 0 :
                                                self.magazine = 50
                                                self.bullets = self.bullets-50
                                        else :
                                                tmp = 50-self.magazine
                                                self.magazine = self.magazine+tmp
                                                self.bullets = self.bullets-tmp

                                else :
                                        if self.magazine == 0 :
                                                self.magazine = self.bullets
                                                self.bullets = 0
                                        else :
                                                if self.magazine+self.bullets > 50 :
                                                        tmp = 50-self.magazine
                                                        self.magazine = self.magazine+tmp
                                                        self.bullets = self.bullets-tmp
                                                else :
                                                        self.magazine += self.bullets
                                                        self.bullets = 0

                                pygame.mixer.Sound("reload.wav").play()
                                while pygame.mixer.get_busy():
                                        pass

                        else :
                                print("Failed to reload. No more bullets")

        def action(self, a):
                if a == "" :
                        if self.magazine > 0 :
                                self.fire()
                        elif self.magazine == 0 and self.bullets > 0 :
                                print("Reload")
                        else :
                                print("End")
                                sys.exit()

                elif a == "r" :
                        self.reload()

                elif a == "e" :
                        print("End")
                        sys.exit()

                if self.magazine == 0 and MachineGun.bullets == 0 :
                        print("End")
                        sys.exit()


if __name__ == '__main__' :
        M = MachineGun()
        print("Ready to fire")
        while True :
                a = input()
                M.action(a)
