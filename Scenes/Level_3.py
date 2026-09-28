import pygame
import sys
from Setting import *

pygame.init()
pygame.mixer.init()

# Configuración de música
pygame.mixer.music.load("Soundtracks/sonic_sand_ocean.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(TITULO3)
reloj = pygame.time.Clock()
ejecutando = True

tile_size = TILE_SIZE

# Carga y escalado de texturas
superficie_piso = pygame.image.load("Assets/bombman/tile_env7_floor.png").convert()
img_cesped = pygame.transform.scale(superficie_piso, (tile_size, tile_size))

superficie_pared = pygame.image.load("Assets/bombman/tile_env7_wall.png").convert()
img_muro = pygame.transform.scale(superficie_pared, (tile_size, tile_size))

superficie_bloque = pygame.image.load("Assets/bombman/tile_env7_block.png").convert_alpha()
img_caja = pygame.transform.scale(superficie_bloque, (tile_size, tile_size))

# Matriz del nivel
nivel_actual = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 2, 1, 0, 0, 0, 1, 0, 0, 0, 1, 2, 0, 1],
    [1, 0, 0, 0, 1, 0, 2, 0, 2, 0, 1, 0, 0, 0, 1],
    [1, 2, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 2, 1],
    [1, 0, 2, 0, 1, 0, 0, 2, 0, 0, 1, 0, 2, 0, 1],
    [1, 2, 0, 2, 0, 1, 2, 2, 2, 1, 0, 2, 0, 2, 1],
    [1, 0, 2, 0, 1, 0, 0, 2, 0, 0, 1, 0, 2, 0, 1],
    [1, 2, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 2, 1],
    [1, 0, 0, 0, 1, 0, 2, 0, 2, 0, 1, 0, 0, 0, 1],
    [1, 0, 2, 1, 0, 0, 0, 1, 0, 0, 0, 1, 2, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Bucle principal
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    
    pantalla.fill(COLOR_FONDO1)

    offset_y = tile_size  
    offset_x = 0   

    for fila_idx, fila in enumerate(nivel_actual):
        for col_idx, valor in enumerate(fila):
            x = int(offset_x + (col_idx * tile_size))
            y = int(offset_y + (fila_idx * tile_size))

            if valor == 0:
                pantalla.blit(img_cesped, (x, y))
            elif valor == 1:
                pantalla.blit(img_muro, (x, y))
            elif valor == 2:
                pantalla.blit(img_caja, (x, y))

    pygame.draw.rect(pantalla, COLOR_BARRA_SUP, (0, 0, ANCHO, tile_size))

    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
sys.exit()