# Programa para calcular estadísticas de calificaciones
def obtener_estadisticas(calificaciones):
    """
    Recibe una lista de calificaciones (números entre 0 y 100)
    y devuelve el promedio, la calificación más alta y la más baja.
    """

    #filtramos las calificaciones 
    calificaciones_validadas = [c for c in calificaciones if 0 <= c <= 100 ]
    #evitamos que se dividan en cero 
    if not calificaciones_validadas:
        return 0,0,0
    #calcular el promedio para obtener la calificacion 
    promedio = sum(calificaciones_validadas) / len(calificaciones_validadas)

    minimo = min(calificaciones_validadas)
    
    maximo = max(calificaciones_validadas)
    
    return promedio, maximo, minimo

def solicitar_calificaciones():
    """
    Solicita al usuario ingresar calificaciones separadas por comas
    y las valida para asegurarse de que sean números entre 0 y 100.
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
    Programa principal: solicita calificaciones, calcula estadísticas y muestra resultados.
    """
    calificaciones = solicitar_calificaciones()  # LLAMAR la función correctamente
    promedio, maximo, minimo = obtener_estadisticas(calificaciones)  # Pasa la lista devuelta
    print("\nEstadísticas de las calificaciones:")
    print("Promedio:", promedio)
    print("Calificación más alta:", maximo)
    print("Calificación más baja:", minimo)

if __name__ == "__main__":
    main()