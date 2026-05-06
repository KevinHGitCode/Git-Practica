def ingresar_notas(estudiantes: dict) -> dict:
    id_est = input("ID del estudiante: ").strip()
    if id_est not in estudiantes:
        print("❌ Estudiante no encontrado.")
        return estudiantes
    asignatura = input("Nombre de la asignatura: ").strip()
    while True:
        try:
            nota = float(input(f"Nota para {asignatura} (0-5): "))
            if 0 <= nota <= 5:
                break
            print("⚠️  La nota debe estar entre 0 y 5.")
        except ValueError:
            print("⚠️  Ingresa un número válido.")
    estudiantes[id_est]["notas"][asignatura] = nota
    print(f"✅ Nota {nota} registrada en {asignatura}.")
    return estudiantes