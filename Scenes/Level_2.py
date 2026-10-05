import pygame
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Setting import *
from Scenes.BaseLevel import BaseLevel

class Level2(BaseLevel):
    def __init__(self):
        super().__init__(2)

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption(TITULO2)
    reloj = pygame.time.Clock()

    # --- ICONOS DE LA BARRA SUPERIOR ---
    iconos = {
        "fuego": pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "icon_flame.png").convert_alpha(), (24, 24)),
        "bomba": pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "icon_bomb.png").convert_alpha(), (24, 24)),
        "velocidad": pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "icon_kicking_shoe.png").convert_alpha(), (24, 24)),
        "vida": pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "icon_vida.png").convert_alpha(), (24, 24))
    }

    nivel = Level2()
    ejecutando = True

    # --- BUCLE PRINCIPAL DEL JUEGO ---
    while ejecutando:
        reloj.tick(FPS)
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                ejecutando = False

        nivel.manejar_eventos(eventos)
        nivel.actualizar()
        nivel.dibujar(pantalla, ANCHO, ALTO, COLOR_FONDO1, COLOR_BARRA_SUP, iconos)
        pygame.display.flip()

    pygame.quit()
    sys.exit()