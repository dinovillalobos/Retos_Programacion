for calificacionV in calificaciones_validadas:
        if 0 <= calificaciones_validadas <= 59:
            print (calificacionV , "F")
        elif  60 <= calificaciones_validadas <= 69:
            print (calificacionV , "D")
        elif  70 <= calificaciones_validadas <= 79:
            print (calificacionV , "C")
        elif  80 <= calificaciones_validadas <= 89:
            print (calificacionV , "B")
        elif  90 <= calificaciones_validadas <= 100:
            print (calificacionV , "A")  