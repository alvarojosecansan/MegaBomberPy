import pygame
import sys
import os
import subprocess

# Configurar la ruta raíz del proyecto
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from Scenes.Setting import *

pygame.init()
pygame.mixer.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(TITULO + " - Menú Principal")
reloj = pygame.time.Clock()

# Cargar fuentes para el menú
try:
    ruta_fuente = RUTA_ASSETS + "VCR_OSD_MONO_1.001.ttf"
    fuente_titulo = pygame.font.Font(ruta_fuente, 38)
    fuente_opciones = pygame.font.Font(ruta_fuente, 24)
    fuente_instruccion = pygame.font.Font(ruta_fuente, 18)
except Exception:
    fuente_titulo = pygame.font.SysFont("Courier New", 36, bold=True)
    fuente_opciones = pygame.font.SysFont("Courier New", 22, bold=True)
    fuente_instruccion = pygame.font.SysFont("Courier New", 18, bold=True)

def mostrar_menu():
    """Dibuja la interfaz del menú principal en pantalla"""
    pantalla.fill(COLOR_FONDO)
    
    t_titulo = fuente_titulo.render("MEGA BOMBER PY", True, (255, 255, 255))
    t_sub = fuente_instruccion.render("SELECCIONA UN NIVEL PARA JUGAR", True, (200, 200, 200))
    
    op1 = fuente_opciones.render("[ 1 ] Nivel 1: Zona de Pruebas", True, (0, 255, 100))
    op2 = fuente_opciones.render("[ 2 ] Nivel 2: Laboratorio Cryo", True, (0, 200, 255))
    op3 = fuente_opciones.render("[ 3 ] Nivel 3: Oasis Perdido", True, (255, 180, 0))
    op_salir = fuente_opciones.render("[ ESC ] Salir del Juego", True, (255, 60, 60))
    
    pantalla.blit(t_titulo, (ANCHO // 2 - t_titulo.get_width() // 2, 140))
    pantalla.blit(t_sub, (ANCHO // 2 - t_sub.get_width() // 2, 200))
    
    pantalla.blit(op1, (ANCHO // 2 - 180, 300))
    pantalla.blit(op2, (ANCHO // 2 - 180, 360))
    pantalla.blit(op3, (ANCHO // 2 - 180, 420))
    pantalla.blit(op_salir, (ANCHO // 2 - 180, 520))

def ejecutar_archivo_nivel(nombre_archivo):
    """Ejecuta el archivo de nivel correspondiente de forma independiente y compatible con el .exe"""
    if getattr(sys, 'frozen', False):
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.dirname(__file__)
        
    ruta_script = os.path.join(base_dir, "Scenes", nombre_archivo)
    
    try:
        subprocess.run([sys.executable, ruta_script])
    except Exception as e:
        print(f"Error al ejecutar el nivel: {e}")

# --- BUCLE PRINCIPAL DEL MENÚ ---
en_menu = True
while en_menu:
    reloj.tick(FPS)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            en_menu = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_1:
                ejecutar_archivo_nivel("Level_1.py")
            elif evento.key == pygame.K_2:
                ejecutar_archivo_nivel("Level_2.py")
            elif evento.key == pygame.K_3:
                ejecutar_archivo_nivel("Level_3.py")
            elif evento.key == pygame.K_ESCAPE:
                en_menu = False

    mostrar_menu()
    pygame.display.flip()

pygame.quit()
sys.exit()