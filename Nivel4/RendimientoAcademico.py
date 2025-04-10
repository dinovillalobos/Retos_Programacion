def validar_calificacion(calificaciones):
    """
    Filtra y devuelve solo las calificaciones que estén entre 0 y 100.
    """
    return [c for c in calificaciones if 0 <= c <= 100]


def clasificar_calificacion(calificacion):
    """
    Clasifica una calificación numérica en una letra (A, B, C, D, F).
    """
    if 90 <= calificacion <= 100:
        return "A"
    elif 80 <= calificacion <= 89:
        return "B"
    elif 70 <= calificacion <= 79:
        return "C"
    elif 60 <= calificacion <= 69:
        return "D"
    else:
        return "F"


def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.
    """
    return sum(calificaciones) / len(calificaciones)


def solicitar_datos():
    """
    Solicita nombres de estudiantes y sus calificaciones.
    Devuelve un diccionario con el formato:
    { "Nombre": [calificaciones] }
    """
    estudiantes = {}
    
    while True:
        nombre = input("Agregar nombre del alumno o escribe 'salir' para finalizar el ingreso: ")
        if nombre.lower() == 'salir':
            break

        try:
            entrada = input(f"Ingresa las calificaciones de {nombre} separadas por comas: ")
            calificaciones = [int(c.strip()) for c in entrada.split(",")]
            calificaciones_validas = validar_calificacion(calificaciones)

            if len(calificaciones_validas) != len(calificaciones):
                print("Se eliminaron calificaciones no válidas fuera del rango de 0-100.")

            estudiantes[nombre] = calificaciones_validas
        
        except ValueError:
            print("Entrada no válida. Usa solo números separados por comas.")
    
    return estudiantes


def mostrar_resumen(estudiantes):
    """
    Muestra un resumen con el promedio y la clasificación de cada estudiante.
    """
    resumen = []

    for nombre, calificaciones in estudiantes.items():
        if calificaciones:
            promedio = calcular_promedio(calificaciones)
            clasificacion = clasificar_calificacion(promedio)
            resumen.append((nombre, promedio, clasificacion))
        else:
            print(f"{nombre} no tiene calificaciones válidas.")

    # Ordenar por promedio de forma descendente
    resumen.sort(key=lambda x: x[1], reverse=True)

    print("\n RESUMEN DE ESTUDIANTES ")
    for nombre, promedio, clasificacion in resumen:
        print(f"{nombre}: Promedio = {promedio:.2f}, Clasificación = {clasificacion}")


def main():
    """
    Función principal del programa.
    """
    print("🎓 Programa de gestión de estudiantes y calificaciones 🎓")
    estudiantes = solicitar_datos()
    mostrar_resumen(estudiantes)


if __name__ == "__main__":
    main()
