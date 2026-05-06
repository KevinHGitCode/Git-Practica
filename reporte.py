def generar_reporte(estudiantes: dict) -> None:
    if not estudiantes:
        print("⚠️  No hay estudiantes registrados.")
        return
    print("\n" + "="*50)
    print(f"{'ID':<10} {'Nombre':<20} {'Promedio':<10} {'Estado'}")
    print("="*50)
    for id_est, datos in estudiantes.items():
        notas = datos["notas"]
        if notas:
            promedio = sum(notas.values()) / len(notas)
            estado = "APROBADO" if promedio >= 3.0 else "REPROBADO"
        else:
            promedio = 0.0
            estado = "SIN NOTAS"
        print(f"{id_est:<10} {datos['nombre']:<20} {promedio:<10.2f} {estado}")
    print("="*50 + "\n")