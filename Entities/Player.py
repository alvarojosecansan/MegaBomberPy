import pygame
from Scenes.Setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.ancho = 65
        self.alto = 65

        # Sprite visual y rectángulo principal
        self.image = pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "player_down.png").convert_alpha(), (self.ancho, self.alto))
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # Hitbox compacta centrada en la parte baja/media del personaje
        self.hitbox = pygame.Rect(x + 13, y + 26, 36, 35)

        # Estadísticas del jugador, Power-ups y Vidas
        self.velocidad = 3.5
        self.limite_bombas = 1      
        self.radio_explosion = 2    
        self.vidas = 3              # Vidas iniciales del jugador
        
        # Control de inmunidad y daño
        self.inmune = False
        self.tiempo_inmunidad = 0   
        self.muriendo = False
        self.frame_muerte = 0
        self.animacion_muerte_timer = 0

        self.direccion = pygame.math.Vector2()
        self.ultima_direccion = "abajo"

        # Carga de sprites estáticos
        self.quieto_abajo = pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "player_down.png").convert_alpha(), (self.ancho, self.alto))
        self.quieto_arriba = pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "player_up.png").convert_alpha(), (self.ancho, self.alto))
        self.quieto_izquierda = pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "player_left.png").convert_alpha(), (self.ancho, self.alto))
        self.quieto_derecha = pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "player_right.png").convert_alpha(), (self.ancho, self.alto))

        # Listas de animación de caminata
        self.caminaAbajo = [
            pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "player_down_walk1.png").convert_alpha(), (self.ancho, self.alto)),
            pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "player_down_walk2.png").convert_alpha(), (self.ancho, self.alto)),
            pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "player_down_walk3.png").convert_alpha(), (self.ancho, self.alto))
        ]

        self.caminaArriba = [
            pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "player_up_walk1.png").convert_alpha(), (self.ancho, self.alto)),
            pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "player_up_walk2.png").convert_alpha(), (self.ancho, self.alto)),
            pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "player_up_walk3.png").convert_alpha(), (self.ancho, self.alto))
        ]

        self.caminaIzquierda = [
            pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "player_left_walk1.png").convert_alpha(), (self.ancho, self.alto)),
            pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "player_left_walk3.png").convert_alpha(), (self.ancho, self.alto))
        ]

        self.caminaDerecha = [
            pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "player_right_walk1.png").convert_alpha(), (self.ancho, self.alto)),
            pygame.transform.scale(pygame.image.load(RUTA_ASSETS + "player_right_walk3.png").convert_alpha(), (self.ancho, self.alto))
        ]

        # Carga de la animación de muerte (animation_die1 a animation_die7)
        self.sprites_muerte = []
        try:
            for i in range(1, 8):
                img_muerte = pygame.transform.scale(
                    pygame.image.load(RUTA_ASSETS + f"animation_die{i}.png").convert_alpha(), 
                    (self.ancho, self.alto)
                )
                self.sprites_muerte.append(img_muerte)
        except Exception as e:
            print(f"Error al cargar sprites de muerte: {e}")

        self.cuentaPasos = 0
        self.moviendose = False
        self.izquierda = False
        self.derecha = False
        self.arriba = False
        self.abajo = False

    def perder_power_ups(self):
        """Reinicia las estadísticas del jugador al recibir daño"""
        self.limite_bombas = 1
        self.radio_explosion = 2
        self.velocidad = 3.5

    def recibir_daño(self):
        """Aplica la lógica de daño si el jugador no es inmune ni está muriendo"""
        if not self.inmune and not self.muriendo:
            self.vidas -= 1
            if self.vidas > 0:
                self.inmune = True
                self.tiempo_inmunidad = 120  # 2 segundos de inmunidad a 60 FPS
                self.perder_power_ups()      # Se pierden las mejoras acumuladas
            else:
                self.muriendo = True
                self.frame_muerte = 0
                self.animacion_muerte_timer = 0

    def teclado(self):
        """Captura de teclas permitiendo una dirección predominante por vez"""
        if self.muriendo:
            return

        keys = pygame.key.get_pressed()
        self.direccion.x = 0
        self.direccion.y = 0
        self.moviendose = False

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direccion.x = -1
            self.izquierda = True
            self.derecha = False
            self.arriba = False
            self.abajo = False
            self.ultima_direccion = "izquierda"
            self.moviendose = True
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direccion.x = 1
            self.izquierda = False
            self.derecha = True
            self.arriba = False
            self.abajo = False
            self.ultima_direccion = "derecha"
            self.moviendose = True
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direccion.y = -1
            self.izquierda = False
            self.derecha = False
            self.arriba = True
            self.abajo = False
            self.ultima_direccion = "arriba"
            self.moviendose = True
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direccion.y = 1
            self.izquierda = False
            self.derecha = False
            self.arriba = False
            self.abajo = True
            self.ultima_direccion = "abajo"
            self.moviendose = True
        else:
            self.cuentaPasos = 0

    def mover(self, velocidad, matriz_nivel):
        """Mueve al personaje separando estrictamente los ejes"""
        if self.direccion.x != 0:
            self.hitbox.x += self.direccion.x * velocidad
            self.colisiones("horizontal", matriz_nivel)

        if self.direccion.y != 0:
            self.hitbox.y += self.direccion.y * velocidad
            self.colisiones("vertical", matriz_nivel)

        self.rect.x = self.hitbox.x - 13
        self.rect.y = self.hitbox.y - 26

    def colisiones(self, direccion, matriz_nivel):
        """Revisa colisiones contra los bloques sólidos (1 y 2)"""
        for fila_idx, fila in enumerate(matriz_nivel):
            for col_idx, valor in enumerate(fila):
                if valor in (1, 2):
                    bloque_rect = pygame.Rect(col_idx * TILE_SIZE, (fila_idx + 1) * TILE_SIZE, TILE_SIZE, TILE_SIZE)

                    if self.hitbox.colliderect(bloque_rect):
                        if direccion == "horizontal":
                            if self.direccion.x > 0:
                                self.hitbox.right = bloque_rect.left
                            elif self.direccion.x < 0:
                                self.hitbox.left = bloque_rect.right

                        if direccion == "vertical":
                            if self.direccion.y > 0:
                                self.hitbox.bottom = bloque_rect.top
                            elif self.direccion.y < 0:
                                self.hitbox.top = bloque_rect.bottom

    def actualizar(self, matriz_nivel):
        if self.inmune:
            self.tiempo_inmunidad -= 1
            if self.tiempo_inmunidad <= 0:
                self.inmune = False

        if self.muriendo:
            return

        self.teclado()
        self.mover(self.velocidad, matriz_nivel)

    def dibujar(self, pantalla):
        pos_dibujo = (self.rect.x, self.rect.y)

        if self.muriendo:
            if self.sprites_muerte:
                imagen_actual = self.sprites_muerte[self.frame_muerte]
                pantalla.blit(imagen_actual, pos_dibujo)
                self.animacion_muerte_timer += 1
                if self.animacion_muerte_timer >= 10:
                    self.animacion_muerte_timer = 0
                    self.frame_muerte += 1
                    if self.frame_muerte >= len(self.sprites_muerte):
                        self.frame_muerte = len(self.sprites_muerte) - 1
            return

        if self.cuentaPasos + 1 >= 18:
            self.cuentaPasos = 0

        if self.izquierda:
            imagen_actual = self.caminaIzquierda[self.cuentaPasos // 9]
            self.cuentaPasos += 1
        elif self.derecha:
            imagen_actual = self.caminaDerecha[self.cuentaPasos // 9]
            self.cuentaPasos += 1
        elif self.arriba:
            imagen_actual = self.caminaArriba[self.cuentaPasos // 6]
            self.cuentaPasos += 1
        elif self.abajo:
            imagen_actual = self.caminaAbajo[self.cuentaPasos // 6]
            self.cuentaPasos += 1
        else:
            if self.ultima_direccion == "izquierda":
                imagen_actual = self.quieto_izquierda
            elif self.ultima_direccion == "derecha":
                imagen_actual = self.quieto_derecha
            elif self.ultima_direccion == "arriba":
                imagen_actual = self.quieto_arriba
            else:
                imagen_actual = self.quieto_abajo

        if self.inmune:
            if (self.tiempo_inmunidad // 10) % 2 == 0:
                imagen_actual = imagen_actual.copy()
                imagen_actual.set_alpha(100)

        pantalla.blit(imagen_actual, pos_dibujo)