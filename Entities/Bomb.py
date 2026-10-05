import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Scenes.Setting import *

class Bomba(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        super().__init__()
        self.tile_size = tile_size
        self.ancho = tile_size
        self.alto = tile_size
        
        self.rect = pygame.Rect(x, y, self.ancho, self.alto)
        self.tiempo_explosion = 180  # 3 segundos a 60 FPS
        self.radio = 2               
        self.activa = True
        
        # --- SPRITES DE ANIMACIÓN ---
        self.sprites_bomba = [
            pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "bomb3.png").convert_alpha(), (self.ancho, self.alto)),
            pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "bomb2.png").convert_alpha(), (self.ancho, self.alto)),
            pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "bomb1.png").convert_alpha(), (self.ancho, self.alto))
        ]
        self.frame_actual = 0

        # --- CARGAR SONIDOS DE EXPLOSIÓN Y CAJAS ---
        try:
            self.sonido_explosion = pygame.mixer.Sound(RUTA_SOUNDTRACKS + "videoplayback-_1_.mp3")
            self.sonido_explosion.set_volume(0.3) 
        except Exception as e:
            self.sonido_explosion = None

        try:
            nombre_archivo_caja = "ytmp3free.cc_wooden-crate-hittakedamage-ver-1-video-game-sfx-free-sound-effects-youtubemp3free.org (1).mp3"
            self.sonido_caja = pygame.mixer.Sound(RUTA_SOUNDTRACKS + nombre_archivo_caja)
            self.sonido_caja.set_volume(0.9)
        except Exception as e:
            self.sonido_caja = None

    # --- ACTUALIZAR TEMPORIZADOR ---
    def actualizar(self, matriz_nivel):
        self.tiempo_explosion -= 1
        
        if self.tiempo_explosion > 120:
            self.frame_actual = 0
        elif self.tiempo_explosion > 60:
            self.frame_actual = 1
        else:
            self.frame_actual = 2

        if self.tiempo_explosion <= 0:
            self.activa = False
            if self.sonido_explosion:
                self.sonido_explosion.play()
            return self.calcular_explosion(matriz_nivel)
            
        return None

    # --- CALCULAR RANGO DE EXPLOSIÓN ---
    def calcular_explosion(self, matriz_nivel):
        col_centro = self.rect.x // self.tile_size
        fila_centro = (self.rect.y // self.tile_size) - 1

        casillas_afectadas = [{"pos": (col_centro, fila_centro), "tipo": "centro", "caja_destruida": False}]

        movimientos = [
            ("arriba", 0, -1),
            ("abajo", 0, 1),
            ("izquierda", -1, 0),
            ("derecha", 1, 0)
        ]

        se_destruyo_caja = False  

        for dir_nombre, dx, dy in movimientos:
            for i in range(1, self.radio + 1):
                c = col_centro + (dx * i)
                f = fila_centro + (dy * i)

                if 0 <= f < len(matriz_nivel) and 0 <= c < len(matriz_nivel[0]):
                    valor_bloque = matriz_nivel[f][c]

                    if valor_bloque == 1: 
                        break 
                    
                    es_extremo = (i == self.radio) or (valor_bloque == 2)
                    es_caja_rota = False

                    if valor_bloque == 2:
                        matriz_nivel[f][c] = 0 
                        se_destruyo_caja = True  
                        es_caja_rota = True

                    if dir_nombre in ("arriba", "abajo"):
                        tipo = f"{dir_nombre}_extremo" if es_extremo else "vertical"
                    else:
                        tipo = f"{dir_nombre}_extremo" if es_extremo else "horizontal"

                    casillas_afectadas.append({
                        "pos": (c, f), 
                        "tipo": tipo, 
                        "caja_destruida": es_caja_rota
                    })

                    if valor_bloque == 2:
                        break
                else:
                    break

        if se_destruyo_caja and self.sonido_caja:
            self.sonido_caja.play(maxtime=3000)

        return casillas_afectadas

    # --- DIBUJAR BOMBA ---
    def dibujar(self, pantalla):
        imagen_actual = self.sprites_bomba[self.frame_actual]
        pantalla.blit(imagen_actual, (self.rect.x, self.rect.y))