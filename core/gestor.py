import json
import os

FILE_PATH = "data/datos.json"


def cargar_datos():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_datos(datos):
    with open(FILE_PATH, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


# LISTAR
def listar_libros():
    return cargar_datos()


# CREAR
def registrar_libro(codigo, titulo, autor):

    datos = cargar_datos()

    for libro in datos:
        if libro["codigo"] == codigo:
            return False, "El código ya existe."

    nuevo = {
        "id": datos[-1]["id"] + 1 if datos else 1,
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "disponible": True
    }

    datos.append(nuevo)
    guardar_datos(datos)

    return True, "Libro registrado correctamente."


# READ
def buscar_libro(codigo):

    datos = cargar_datos()

    for libro in datos:
        if libro["codigo"] == codigo:
            return libro

    return None


# UPDATE
def actualizar_libro(codigo, titulo, autor):

    datos = cargar_datos()

    for libro in datos:
        if libro["codigo"] == codigo:

            libro["titulo"] = titulo
            libro["autor"] = autor

            guardar_datos(datos)

            return True

    return False


# DELETE
def eliminar_libro(codigo):

    datos = cargar_datos()

    nuevos = [libro for libro in datos if libro["codigo"] != codigo]

    if len(nuevos) == len(datos):
        return False

    guardar_datos(nuevos)

    return True


# PRESTAR
def prestar_libro(codigo):

    datos = cargar_datos()

    for libro in datos:

        if libro["codigo"] == codigo:

            if libro["disponible"]:
                libro["disponible"] = False
                guardar_datos(datos)
                return True, "Libro prestado correctamente."

            return False, "Libro ya prestado."

    return False, "Libro no encontrado."


# DEVOLVER
def devolver_libro(codigo):

    datos = cargar_datos()

    for libro in datos:

        if libro["codigo"] == codigo:

            if not libro["disponible"]:
                libro["disponible"] = True
                guardar_datos(datos)
                return True, "Libro devuelto correctamente."

            return False, "El libro ya estaba disponible."

    return False, "Libro no encontrado."


# ESTADISTICAS
def obtener_estadisticas():

    datos = cargar_datos()

    total = len(datos)

    disponibles = 0
    prestados = 0

    for libro in datos:

        if libro["disponible"]:
            disponibles += 1
        else:
            prestados += 1

    return {
        "total": total,
        "disponibles": disponibles,
        "prestados": prestados
    }