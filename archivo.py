import json
import os

def guardar_datos(estudiantes: dict, nombre_archivo: str = "datos.json") -> None:
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(estudiantes, f, ensure_ascii=False, indent=4)
    print(f"✅ Datos guardados en '{nombre_archivo}'.")

def cargar_datos(nombre_archivo: str = "datos.json") -> dict:
    if not os.path.exists(nombre_archivo):
        print("⚠️  No se encontró archivo de datos. Iniciando vacío.")
        return {}
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        datos = json.load(f)
    print(f"✅ Datos cargados desde '{nombre_archivo}'.")
    return datos