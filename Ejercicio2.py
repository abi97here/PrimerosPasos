""" En este ejercicio queremos sumar la cantidad de alumnos regulares, más la cantidad de alumnos recursantes,
pero al imprimir el resultado por pantalla se nos presentan dos resultados sin aclaración alguna.
 Esto hace que el programa sea confuso"""


"""cantidad_alumnos = 8
cantidad_recursantes = 2
print(cantidad_alumnos)

total_alumnos = cantidad_alumnos + cantidad_recursantes
print(total_alumnos)"""

""" En esta parte vamos a realizar ajustes al código para que podamos tener un programa claro"""

alumnos_regulares = 8
alumnos_recursantes = 2

print(f"La cantidad de alumnos regulares es: {alumnos_regulares}")

cantidad_total = alumnos_regulares + alumnos_recursantes
print(f"La cantidad total de alumnos es: {cantidad_total}")
