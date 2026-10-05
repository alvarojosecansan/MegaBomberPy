import pygame
import os
import sys

# Detectar si estamos ejecutando un archivo compilado (.exe) o script normal
if getattr(sys, 'frozen', False):
    # Si es un ejecutable compilado con PyInstaller
    BASE_DIR = sys._MEIPASS
else:
    # Si estamos ejecutando el código fuente en Python
    # (Apunta a la carpeta raíz del proyecto independientemente de dónde esté)
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# --- Configuración de la Ventana ---
ANCHO = 840
ALTO = 784
FPS = 60

TITULO = "Mega Bomber Py"
TITULO1 = "Nivel 1: Zona de Pruebas"
TITULO2 = "Nivel 2: Laboratorio Cryo"
TITULO3 = "Nivel 3: Oasis Perdido"

# --- Colores (RGB) ---
COLOR_FONDO = (1, 1, 3)
COLOR_FONDO1 = (255, 255, 255)
COLOR_BARRA_SUP = (0, 0, 0)

# --- Configuración de Tiles y Rutas Dinámicas ---
TILE_SIZE = 56
RUTA_ASSETS = os.path.join(BASE_DIR, "Assets", "bombman") + os.sep
RUTA_SOUNDTRACKS = os.path.join(BASE_DIR, "Soundtracks") + os.sep