import pygame
import random
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Scenes.Setting import *

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size, tipo_forzado=None):
        super().__init__()
        self.tile_size = tile_size
        self.ancho = tile_size
        self.alto = tile_size
        
        self.rect = pygame.Rect(x, y, self.ancho, self.alto)
        
        tipos_disponibles = ["bomba", "fuego", "velocidad", "vida"]
        self.tipo = tipo_forzado if tipo_forzado else random.choice(tipos_disponibles)
        
        try:
            if self.tipo == "bomba":
                imagen_archivo = "item_bomb.png"
            elif self.tipo == "fuego":
                imagen_archivo = "item_flame.png"
            elif self.tipo == "velocidad":
                imagen_archivo = "item_shoe.png"
            elif self.tipo == "vida":
                imagen_archivo = "icon_heart.png"
            else:
                imagen_archivo = "item_flame.png"
                
            self.image = pygame.transform.scale(
                pygame.image.load(RUTA_ASSETS + imagen_archivo).convert_alpha(), 
                (self.ancho, self.alto)
            )
        except Exception as e:
            print(f"No se pudo cargar la imagen del item {self.tipo}: {e}")
            self.image = pygame.Surface((self.ancho, self.alto))
            self.image.fill((255, 255, 0))

    def aplicar_efecto(self, jugador):
        if self.tipo == "bomba":
            jugador.limite_bombas = min(jugador.limite_bombas + 1, 2)
        elif self.tipo == "fuego":
            jugador.radio_explosion += 1
        elif self.tipo == "velocidad":
            jugador.velocidad += 0.7
        elif self.tipo == "vida":
            jugador.vidas = min(jugador.vidas + 1, 4)

    def dibujar(self, pantalla):
        pantalla.blit(self.image, (self.rect.x, self.rect.y))