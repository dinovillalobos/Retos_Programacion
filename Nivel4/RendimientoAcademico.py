def validar_calificacion(calificaciones):
    return [c for c in calificaciones if 0 <= c <= 100]

def clasificar_calificacion(calificacion):
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
    calificaciones_validas = validar_calificacion(calificaciones)
    if not calificaciones_validas:
        return 0
    return sum(calificaciones_validas) / len(calificaciones_validas)

def solicitar_datos():
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
            print("Entrada no válida. Intenta de nuevo.")
    return estudiantes

def mostrar_resumen(estudiantes):
    resumen = []
    for nombre, calificaciones in estudiantes.items():
        if calificaciones:
            promedio = calcular_promedio(calificaciones)
            clasificacion = clasificar_calificacion(promedio)
            resumen.append((nombre, promedio, clasificacion))
        else:
            print(f"{nombre} no tiene calificaciones válidas.")
    
    resumen.sort(key=lambda x: x[1], reverse=True)

    print("\n RESUMEN DE ESTUDIANTES")
    for nombre, promedio, clasificacion in resumen:
        print(f"{nombre}: Promedio = {promedio:.2f}, Clasificación = {clasificacion}")

def main():
    print("Programa de gestión de estudiantes y calificaciones")
    estudiantes = solicitar_datos()
    mostrar_resumen(estudiantes)

if __name__ == "__main__":
    main()
