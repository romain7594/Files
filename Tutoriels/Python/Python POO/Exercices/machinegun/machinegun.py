import pygame

pygame.mixer.init()

# ............
# ............

pygame.mixer.Sound("fire.wav").play()
while pygame.mixer.get_busy():
	pass
