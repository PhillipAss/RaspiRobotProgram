# -*- coding: UTF-8 -*-

 

# Pygame-Modul importieren.

import pygame
from rrb3 import *
import time


rr=RRB3(9,6)
rr.set_led1(1)
rr.set_led1(0)
rr.set_led2(1)
rr.set_led2(0)
rr.sw1_closed()
rr.stop()
i=0
# Initialisieren aller Pygame-Module und    

# Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).

pygame.init()

screen = pygame.display.set_mode((800, 600))



# Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.

pygame.display.set_caption("RASPIROBOTBOARD KONTROLLCENTER")

pygame.mouse.set_visible(1)

pygame.key.set_repeat(1, 30)



# Clock-Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.

clock = pygame.time.Clock()



# Die Schleife, und damit unser Spiel, läuft solange running == True.

running = True

while running:

	# Framerate auf 30 Frames pro Sekunde beschränken.

	# Pygame wartet, falls das Programm schneller läuft.

	clock.tick(30)



	# screen-Surface mit Schwarz (RGB = 0, 0, 0) füllen.

	screen.fill((0, 0, 0))

	i = rr.get_distance()
	time.sleep(0.25)
	
	if i < 40:
		rr.stop()
	else:
		rr.set_motors(0.25,0,0.25,0)

	# Alle aufgelaufenen Events holen und abarbeiten.

	for event in pygame.event.get():

		# Spiel beenden, wenn wir ein QUIT-Event finden.

		if event.type == pygame.QUIT:

			running = False

		

		# Wir interessieren uns auch für "Taste gedrückt"-Events.

		if event.type == pygame.KEYDOWN:
			

			# Wenn Escape gedrückt wird, posten wir ein QUIT-Event in Pygames Event-Warteschlange.

			if event.key == pygame.K_ESCAPE:

				pygame.event.post(pygame.event.Event(pygame.QUIT))

			if event.key == pygame.K_UP:	
				rr.set_motors(0.25,0,0.25,0)

                        if event.key == pygame.K_LEFT:
				rr.set_motors(0.25,0,0.05,0)

			if event.key == pygame.K_RIGHT:
				rr.set_motors(0.05,0,0.25,0)

			if event.key == pygame.K_DOWN:
				rr.stop()
				
				

	# Inhalt von screen anzeigen.

	pygame.display.flip()

 

 

# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.


