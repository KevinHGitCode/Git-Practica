def registrar_estudiante(estudiantes: dict) -> dict:
    nombre = input("Nombre del estudiante: ").strip()
    id_est = input("ID del estudiante: ").strip()
    if id_est in estudiantes:
        print("⚠️  Ya existe un estudiante con ese ID.")
        return estudiantes
    estudiantes[id_est] = {"nombre": nombre, "notas": {}}
    print(f"✅ Estudiante '{nombre}' registrado.")
    return estudiantes