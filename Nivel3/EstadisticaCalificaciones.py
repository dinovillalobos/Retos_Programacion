def validar_calificaciones(calificaciones):
    """
    Valida que cada calificación esté entre 0 y 100.
    Devuelve una lista de calificaciones válidas.
    """
    return [c for c in calificaciones if 0 <= c <= 100 ]

def clasificar_calificaciones (calificacion):
    """
    Clasifica una calificación según la escala definida.
    """
    if 90 <= calificacion <= 100:
        return "A"
    elif  80 <= calificacion <= 89:
        return "B"
    elif  70 <= calificacion <= 79:
        return "C"
    elif  60 <= calificacion <= 69:
        return "D"
    else:
        return "F"


def solicitar_calificaciones():
    """
    Solicita al usuario una lista de calificaciones separadas por comas
    y convierte la entrada en una lista de números enteros.
    """
    while True:
        try:
            entrada = input("Ingresa las calificaciones separadas por comas: ")
            calificaciones = [int(c.strip()) for c in entrada.split(",")]
            return calificaciones  # Devuelve la lista de calificaciones
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar números separados por comas.")


def main():
    """
    Programa principal: Solicita calificaciones, las clasifica y muestra resultados.
    """
    calificaciones = solicitar_calificaciones()
    calificaciones_validadas = validar_calificaciones(calificaciones)

    if not calificaciones_validadas:
        print("No se ingresaron calificaciones válidas.")
        return
    
    print("\nResultados:")
    for calificacion in calificaciones_validadas:
        clasificacion = clasificar_calificaciones(calificacion)
        print(f"{calificacion} -> {clasificacion}")

if __name__ == "__main__":
    main()