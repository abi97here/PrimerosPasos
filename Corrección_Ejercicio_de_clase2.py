
#Realicé corrección a este ejercicio porque el ingreso_promedio me daba un resultado incorrecto, 
#me faltó abrir y cerrar paréntesis en la operación de suma de ingresos mensuales.

# ingreso promedio
# Escribir un programa que guarde en variables el monto
# del ingreso de cada uno de los primeros 6 meses del año.
# Luego, calcular y guardar en otra variable el promedio de esos valores.
# Por último, mostrar una leyenda que diga “El ingreso promedio en el 
# semestre es de xxxxx” donde “xxxxx” es el valor calculado.

ingreso_enero = 10000
ingreso_febrero = 12000
ingreso_marzo = 11000
ingreso_abril = 13000
ingreso_mayo = 14000
ingreso_junio = 15000

ingreso_promedio = (ingreso_enero + ingreso_febrero + ingreso_marzo + ingreso_abril + ingreso_mayo + ingreso_junio) / 6
print(f"El ingreso promedio del primer semestre del año es: {ingreso_promedio}")
