"""🧱 Nivel 1 - Día 1: Código Legible y Ordenado (Python o C#)
🎯 Objetivo:
Escribir código claro, con nombres de variables descriptivos, buena indentación, y comentarios que expliquen el por qué, no el cómo.

🔍 Desafío:
Crea un programa que reciba una lista de calificaciones de alumnos (entre 0 y 100), y devuelva:

El promedio.

La calificación más alta.

La calificación más baja.

👉 Usa buenas prácticas:

Nombres de variables claros.

Comentarios donde haga falta.

Código bien indentado.

Nada de cosas como a = 10 si no se sabe qué es a.

📝 Extra (opcional):
Si terminas rápido, agrega una opción para ingresar las calificaciones desde consola, separadas por comas."""


# Programa para calcular estadísticas de calificaciones

def obtener_estadisticas(calificaciones):
    """
    Recibe una lista de calificaciones (números entre 0 y 100)
    y devuelve el promedio, la calificación más alta y la más baja.
    """
    # Aquí irá la lógica

    #validar calificaciones
    calificaciones_validadas = [c for c in calificaciones if 0 <= c <= 100 ]

    if not calificaciones_validadas:
        return 0,0,0

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
