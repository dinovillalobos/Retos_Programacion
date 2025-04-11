def solicitar_estudiantes():
    """
    Solicita al usuario ingresar nombres de estudiantes.
    Devuelve una lista con los nombres ingresados.
    """
    estudiantes = []
    while True:
        nombre = input("Ingresa el nombre del estudiante (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        if nombre:  # Evita entradas vacías
            estudiantes.append(nombre)
    return estudiantes

def registrar_asistencia(estudiantes, dias=3):
    """
    Registra asistencia y participación de cada estudiante durante varios días.
    Devuelve un diccionario con la estructura:
    {
        'nombre': {
            'asistencia': [True, False, True],
            'participacion': [True, False, True]
        }
    }
    """
    registro = {}

    for estudiante in estudiantes:
        print(f"\n👨‍🏫 Registro de {estudiante}")
        asistencias = []
        participaciones = []

        for dia in range(1, dias + 1):
            # Validar entrada para asistencia
            while True:
                asistencia = input(f"¿Asistió el día {dia}? (sí/no): ").strip().lower()
                if asistencia in ['sí', 'si', 'no']:
                    asistencias.append(asistencia.startswith('s'))
                    break
                else:
                    print("Respuesta inválida. Escribe 'sí' o 'no'.")
            
            # Validar participación solo si asistió
            if asistencias[-1]:
                while True:
                    participacion = input(f"¿Participó el día {dia}? (sí/no): ").strip().lower()
                    if participacion in ['sí', 'si', 'no']:
                        participaciones.append(participacion.startswith('s'))
                        break
                    else:
                        print("Respuesta inválida. Escribe 'sí' o 'no'.")
            else:
                participaciones.append(False)

        registro[estudiante] = {
            'asistencia': asistencias,
            'participacion': participaciones
        }

    return registro

def mostrar_resumen(registro):
    """
    Muestra un resumen del porcentaje de asistencia y participación por estudiante.
    """
    print("\n📋 RESUMEN DE ASISTENCIA Y PARTICIPACIÓN")
    for estudiante, datos in registro.items():
        total_dias = len(datos['asistencia'])
        asistencias = sum(datos['asistencia'])
        participaciones = sum(datos['participacion'])

        porcentaje_asistencia = (asistencias / total_dias) * 100
        porcentaje_participacion = (participaciones / asistencias * 100) if asistencias > 0 else 0

        print(f"\n{estudiante}:")
        print(f"Asistió {asistencias}/{total_dias} días ({porcentaje_asistencia:.2f}%)")
        print(f"Participó {participaciones} veces ({porcentaje_participacion:.2f}%)")

def main():
    print("📚 Sistema de Registro de Asistencia y Participación")
    estudiantes = solicitar_estudiantes()
    if estudiantes:
        registro = registrar_asistencia(estudiantes)
        mostrar_resumen(registro)
    else:
        print("No se ingresaron estudiantes.")

if __name__ == "__main__":
    main()
