import pygame
import random
import os
import sys

# Configuración de rutas globales
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Setting import *
from Entities.Player import Player
from Entities.Bomb import Bomba
from Entities.Items import Item

class BaseLevel:
    def __init__(self, numero_nivel):
        self.numero_nivel = numero_nivel
        
        # --- CARGAR AUDIO DE POWER-UPS ---
        try:
            self.sonido_item = pygame.mixer.Sound("Soundtracks/ytmp3free (mp3cut.net).mp3")
            self.sonido_item.set_volume(0.5)
        except Exception as e:
            self.sonido_item = None
        
        # --- CONFIGURACIÓN DE MAPAS Y MATRICES ---
        if self.numero_nivel == 1:
            self.matriz_original = [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 1],
                [1, 0, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 1],
                [1, 2, 1, 2, 1, 2, 1, 0, 1, 2, 1, 2, 1, 2, 1],
                [1, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 1],
                [1, 2, 1, 2, 1, 2, 1, 0, 1, 2, 1, 2, 1, 2, 1],
                [1, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 1],
                [1, 0, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 1],
                [1, 0, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 0, 1], 
                [1, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 1], 
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ]
            musica_ruta = "Soundtracks/portal2_science_is_fun.mp3"
            piso_img = "Assets/bombman/tile_env1_floor.png"
            muro_img = "Assets/bombman/tile_env1_wall.png"
            caja_img = "Assets/bombman/tile_env1_block.png"
            
        elif self.numero_nivel == 2:
            self.matriz_original = [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 2, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1],
                [1, 0, 2, 2, 0, 0, 0, 2, 0, 0, 0, 1, 0, 2, 1],
                [1, 0, 0, 2, 0, 0, 1, 1, 1, 0, 2, 2, 2, 2, 1],
                [1, 0, 2, 2, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 1],
                [1, 0, 0, 1, 1, 1, 0, 2, 0, 1, 1, 1, 0, 0, 1],
                [1, 2, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 2, 1],
                [1, 0, 2, 2, 2, 2, 0, 2, 0, 2, 2, 2, 2, 0, 1],
                [1, 0, 0, 2, 2, 2, 0, 2, 0, 2, 2, 2, 0, 0, 1],
                [1, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 1],
                [1, 0, 2, 1, 1, 1, 0, 2, 0, 1, 1, 1, 2, 0, 1],
                [1, 0, 0, 2, 2, 2, 0, 2, 0, 2, 2, 2, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ]
            musica_ruta = "Soundtracks/sonic_icecap.mp3"
            piso_img = "Assets/bombman/tile_env6_floor.png"
            muro_img = "Assets/bombman/tile_env6_wall.png"
            caja_img = "Assets/bombman/tile_env6_block.png"
            
        elif self.numero_nivel == 3:
            self.matriz_original = [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 1],
                [1, 0, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 0, 1],
                [1, 2, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 1],
                [1, 0, 1, 2, 1, 0, 1, 0, 1, 0, 1, 2, 1, 0, 1],
                [1, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 1],
                [1, 0, 1, 2, 1, 0, 1, 0, 1, 0, 1, 2, 1, 0, 1],
                [1, 2, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 1],
                [1, 0, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 0, 1],
                [1, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ]
            musica_ruta = "Soundtracks/sonic_sand_ocean.mp3"
            piso_img = "Assets/bombman/tile_env7_floor.png"
            muro_img = "Assets/bombman/tile_env7_wall.png"
            caja_img = "Assets/bombman/tile_env7_block.png"

        self.nivel_actual = [fila[:] for fila in self.matriz_original]
        ts = TILE_SIZE

        # --- CARGAR TEXTURAS DE LOS TILES ---
        self.texturas_mapa = {
            "piso": pygame.transform.scale(pygame.image.load(piso_img).convert(), (ts, ts)),
            "muro": pygame.transform.scale(pygame.image.load(muro_img).convert(), (ts, ts)),
            "caja": pygame.transform.scale(pygame.image.load(caja_img).convert_alpha(), (ts, ts)),
            "flama_centro": pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "flame1.png").convert_alpha(), (ts, ts)),
            "flama_horizontal": pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "flame1_horizontal.png").convert_alpha(), (ts, ts)),
            "flama_vertical": pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "flame1_vertical.png").convert_alpha(), (ts, ts)),
            "flama_arriba_extremo": pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "flame1_up.png").convert_alpha(), (ts, ts)),
            "flama_abajo_extremo": pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "flame1_down.png").convert_alpha(), (ts, ts)),
            "flama_izquierda_extremo": pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "flame1_left.png").convert_alpha(), (ts, ts)),
            "flama_derecha_extremo": pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "flame1_right.png").convert_alpha(), (ts, ts)),
        }

        self.tile_size = ts 
        self.jugador = Player(1 * self.tile_size, 2 * self.tile_size)
        self.puntuacion = 0
        self.tiempo_restante = 200
        self.contador_frames_tiempo = 0
        self.vida_extra_spawned = False
        
        self.lista_bombas = []
        self.fuegos_activos = []
        self.lista_items = []
        self.duracion_fuego = 20
        self.game_over = False

        # --- CONFIGURACIÓN DE FUENTES Y MÚSICA ---
        ruta_fuente = "Assets/bombman/VCR_OSD_MONO_1.001.ttf"
        try:
            self.fuente_grande = pygame.font.Font(ruta_fuente, 42)
            self.fuente_mediana = pygame.font.Font(ruta_fuente, 27)
            self.fuente_peque = pygame.font.Font(ruta_fuente, 20)
        except Exception:
            self.fuente_grande = pygame.font.SysFont("Courier New", 42, bold=True)
            self.fuente_mediana = pygame.font.SysFont("Courier New", 24, bold=True)
            self.fuente_peque = pygame.font.SysFont("Courier New", 20, bold=True)

        try:
            pygame.mixer.music.load(musica_ruta)
            pygame.mixer.music.set_volume(0.2 if self.numero_nivel == 1 else 0.4)
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Error cargando música: {e}")

    # --- CONTROL DE EVENTOS Y TECLADO ---
    def manejar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if self.game_over:
                    if evento.key == pygame.K_SPACE:
                        self.reiniciar()
                else:
                    if evento.key == pygame.K_e and len(self.lista_bombas) < getattr(self.jugador, 'limite_bombas', 1):
                        bomba_x = (self.jugador.hitbox.centerx // self.tile_size) * self.tile_size
                        bomba_y = (self.jugador.hitbox.centery // self.tile_size) * self.tile_size
                        radio_bomba = getattr(self.jugador, 'radio_explosion', 2)
                        nueva_bomba = Bomba(bomba_x, bomba_y, self.tile_size)
                        nueva_bomba.radio = radio_bomba
                        self.lista_bombas.append(nueva_bomba)

    # --- REINICIO DE PARTIDA ---
    def reiniciar(self):
        self.jugador = Player(1 * self.tile_size, 2 * self.tile_size)
        self.puntuacion = 0
        self.tiempo_restante = 200
        self.vida_extra_spawned = False
        self.nivel_actual = [fila[:] for fila in self.matriz_original]
        self.lista_bombas.clear()
        self.fuegos_activos.clear()
        self.lista_items.clear()
        self.game_over = False

    # --- BUCLE DE ACTUALIZACIÓN LÓGICA ---
    def actualizar(self):
        if self.game_over:
            return

        self.contador_frames_tiempo += 1
        if self.contador_frames_tiempo >= 60:
            self.contador_frames_tiempo = 0
            if self.tiempo_restante > 0:
                self.tiempo_restante -= 1

        self.jugador.actualizar(self.nivel_actual)

        if self.jugador.muriendo and self.jugador.frame_muerte >= len(self.jugador.sprites_muerte) - 1:
            self.game_over = True

        # Actualizar bombas y verificar explosiones
        for bomba in self.lista_bombas[:]:
            resultado_explosion = bomba.actualizar(self.nivel_actual)
            if not bomba.activa:
                if bomba in self.lista_bombas:
                    self.lista_bombas.remove(bomba)
                if resultado_explosion:
                    self.fuegos_activos.append({"casillas": resultado_explosion, "timer": self.duracion_fuego})
                    
                    cajas_rotas = [casilla for casilla in resultado_explosion if casilla.get("caja_destruida", False)]
                    if cajas_rotas:
                        self.puntuacion += len(cajas_rotas) * 100
                        
                        # Generación aleatoria de power-ups al romper cajas (38%)
                        if random.random() < 0.38:
                            caja_elegida = random.choice(cajas_rotas)
                            
                            tipos_en_pantalla = [item.tipo for item in self.lista_items]
                            tipos_disponibles = []
                            pesos = []
                            
                            if not self.vida_extra_spawned and "vida" not in tipos_en_pantalla and random.random() < 0.10:
                                tipos_disponibles.append("vida")
                                pesos.append(1.0)
                                self.vida_extra_spawned = True
                            else:
                                if getattr(self.jugador, 'limite_bombas', 1) == 1 and "bomba" not in tipos_en_pantalla:
                                    tipos_disponibles.append("bomba")
                                    pesos.append(0.30)
                                if getattr(self.jugador, 'radio_explosion', 2) == 2 and "fuego" not in tipos_en_pantalla:
                                    tipos_disponibles.append("fuego")
                                    pesos.append(0.35)
                                if getattr(self.jugador, 'velocidad', 3.5) == 3.5 and "velocidad" not in tipos_en_pantalla:
                                    tipos_disponibles.append("velocidad")
                                    pesos.append(0.35)
                            
                            if tipos_disponibles:
                                tipo_elegido = random.choices(tipos_disponibles, weights=pesos, k=1)[0]
                                c, f = caja_elegida["pos"]
                                self.lista_items.append(Item(c * self.tile_size, (f + 1) * self.tile_size, self.tile_size, tipo_forzado=tipo_elegido))

        # Actualizar fuegos y daño al jugador
        for fuego in self.fuegos_activos[:]:
            fuego["timer"] -= 1
            for item in fuego["casillas"]:
                c, f = item["pos"]
                fuego_rect = pygame.Rect(c * self.tile_size, (f + 1) * self.tile_size, self.tile_size, self.tile_size)
                if self.jugador.hitbox.colliderect(fuego_rect):
                    self.jugador.recibir_daño()
                    self.jugador.limite_bombas = 1
                    self.jugador.radio_explosion = 2
            if fuego["timer"] <= 0:
                self.fuegos_activos.remove(fuego)

        # Colisión con ítems
        for item in self.lista_items[:]:
            if self.jugador.hitbox.colliderect(item.rect):
                item.aplicar_efecto(self.jugador)
                self.puntuacion += 500
                if self.sonido_item:
                    self.sonido_item.play()
                self.lista_items.remove(item)

    # --- RENDERIZADO Y DIBUJADO EN PANTALLA ---
    def dibujar(self, pantalla, ancho, alto, color_fondo, color_barra, iconos):
        pantalla.fill(color_fondo)

        for fila_idx, fila in enumerate(self.nivel_actual):
            for col_idx, valor in enumerate(fila):
                x = col_idx * self.tile_size
                y = (fila_idx + 1) * self.tile_size
                if valor == 0:
                    pantalla.blit(self.texturas_mapa["piso"], (x, y))
                elif valor == 1:
                    pantalla.blit(self.texturas_mapa["muro"], (x, y))
                elif valor == 2:
                    pantalla.blit(self.texturas_mapa["caja"], (x, y))

        for item in self.lista_items:
            item.dibujar(pantalla)
        for bomba in self.lista_bombas:
            bomba.dibujar(pantalla)
        
        for fuego in self.fuegos_activos:
            for item in fuego["casillas"]:
                c, f = item["pos"]
                tipo = item["tipo"]
                pantalla.blit(self.texturas_mapa[f"flama_{tipo}"], (c * self.tile_size, (f + 1) * self.tile_size))

        self.jugador.dibujar(pantalla)

        # HUD superior (Puntuación, Tiempo, Vidas e Iconos)
        pygame.draw.rect(pantalla, color_barra, (0, 0, ancho, self.tile_size))
        pantalla.blit(self.fuente_mediana.render(f"{self.puntuacion:08d}", True, (255, 255, 255)), (55, 12))
        pantalla.blit(self.fuente_mediana.render(f"T:{self.tiempo_restante}", True, (255, 255, 255)), (260, 12))
        pantalla.blit(self.fuente_mediana.render(f"VIDAS:{max(0, self.jugador.vidas)}", True, (255, 255, 255)), (415, 12))

        ox = 600
        if getattr(self.jugador, 'radio_explosion', 2) > 2 and iconos.get("fuego"):
            pantalla.blit(iconos["fuego"], (ox, 10))
            ox += 35
        if getattr(self.jugador, 'limite_bombas', 1) > 1 and iconos.get("bomba"):
            pantalla.blit(iconos["bomba"], (ox, 10))
            ox += 35
        if getattr(self.jugador, 'velocidad', 3.5) > 3.5 and iconos.get("velocidad"):
            pantalla.blit(iconos["velocidad"], (ox, 10))
            ox += 35
        if getattr(self.jugador, 'vidas', 3) > 3 and iconos.get("vida"):
            pantalla.blit(iconos["vida"], (ox, 10))

        # Pantalla de Game Over
        if self.game_over:
            s = pygame.Surface((ancho, alto), pygame.SRCALPHA)
            s.fill((0, 0, 0, 180))
            pantalla.blit(s, (0, 0))
            tg = self.fuente_grande.render("GAME OVER", True, (255, 40, 40))
            tp = self.fuente_peque.render("PRESIONA ESPACIO PARA REPETIR EL NIVEL", True, (255, 255, 255))
            pantalla.blit(tg, (ancho // 2 - tg.get_width() // 2, alto // 2 - 40))
            pantalla.blit(tp, (ancho // 2 - tp.get_width() // 2, alto // 2 + 20))