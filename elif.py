calificacion = int(input("calificación: "))
residuo = calificacion % 10

if residuo > 5:
    calificacion = int(calificacion) - residuo + 10
    print(calificacion)
elif residuo < 5:
    calificacion = int(calificacion) - residuo
    print(calificacion)
else:
    print("Tu calificación no amerita redondeo.")


