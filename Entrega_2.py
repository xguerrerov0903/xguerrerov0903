'''
Determinar el estado de aprobación:
Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada

Calcular el promedio:
Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
Calcular y mostrar el promedio de las calificaciones en la lista

Contar calificaciones mayores:
Preguntar al usuario por un valor específico
Contar cuántas calificaciones en la lista son mayores que este valor

Verificar y contar calificaciones específicas:
Preguntar al usuario por un valor específico
Contar cuántas calificaciones en la lista son este valor
'''

while True:
    try:
        entrada = input("Ingresa tus notas separados por comas (0 al 100): ")
        valores = [x.strip() for x in entrada.split(",")]
        



    except ValueError:
        print("Cadena de valores invalida")

numeros = []

# Intentar convertir cada valor a float y verificar el rango
valido = True
for x in valores:
    try:
        num = float(x)
        if 0 <= num <= 100:
            numeros.append(num)
        else:
            print(f"El número {num} está fuera del rango permitido (0-100).")
            valido = False
    except ValueError:
        print(f"'{x}' no es un número válido.")
        valido = False

# Si todos los valores son válidos y en rango, puedes continuar
if valido:
    print("Lista de números válidos:", numeros)
else:
    print("La entrada contenía valores no válidos o fuera de rango.")
