import json
import os

ARCHIVO = "data/biblioteca.json"

def cargar_datos():
    # Si el archivo no existe, devolvemos una lista vacía
    if not os.path.exists(ARCHIVO):
        return []
    
    # Abrimos el archivo y cargamos la lista de libros
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_datos(libros):
    # Guardamos la lista de libros en el archivo JSON
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(libros, f, indent=4, ensure_ascii=False)

