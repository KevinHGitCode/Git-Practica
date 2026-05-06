def calcular_promedio(estudiantes: dict) -> None:
    id_est = input("ID del estudiante: ").strip()
    if id_est not in estudiantes:
        print("❌ Estudiante no encontrado.")
        return
    notas = estudiantes[id_est]["notas"]
    if not notas:
        print("⚠️  El estudiante no tiene notas registradas.")
        return
    promedio = sum(notas.values()) / len(notas)
    estado = "✅ APROBADO" if promedio >= 3.0 else "❌ REPROBADO"
    nombre = estudiantes[id_est]["nombre"]
    print(f"\n📊 {nombre} — Promedio: {promedio:.2f} — {estado}")