import pygame
import sys
from Scenes.Setting import *

pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(TITULO)
reloj = pygame.time.Clock()

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill(COLOR_FONDO)
    pygame.display.flip()
    reloj.tick(FPS)

# Salida limpia
pygame.quit()
sys.exit()