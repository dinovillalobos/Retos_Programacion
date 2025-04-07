
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


def main():
    # Lista de ejemplo (puedes cambiarla o pedirla al usuario)
    calificaciones = [85, 92, 78, 90, 88]

    # Llamar la función y mostrar resultados
    promedio, maximo, minimo = obtener_estadisticas(calificaciones)

    print("Promedio:", promedio)
    print("Calificación más alta:", maximo)
    print("Calificación más baja:", minimo)


if __name__ == "__main__":
    main()
