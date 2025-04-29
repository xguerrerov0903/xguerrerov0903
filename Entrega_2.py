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


import sys

def num_valido ():
    while True:
        try:
            nota = float(input("Ingresa la nota (0 a 100): "))
            if nota>=0 and nota<=100:
                return nota
                break
            else:
                print("Valor invalido")
        except ValueError:
            print("Valor invalido")

def aprobado (nota, aprobacion):
    if (nota>=aprobacion):
        return True
    else:
        return False

def cadena_notas ():
    while True:
        try:
            entrada = input("Ingresa tus notas separados por comas (0 al 100): ")
            
            valores = []
            for x in entrada.split(","):
                if 0 <= float(x.strip()) <= 100:
                    valores.append(float(x.strip()))
                else:
                    raise ValueError("Nota fuera de rango")
            break
                    
        except ValueError:
            print("Cadena de valores invalida")
    return valores      

def promedio_notas (lista_notas):
    suma_notas = 0
    for x in lista_notas:
        suma_notas += x
    return suma_notas/len(lista_notas)

def mayor_nota (cadena_nota, mayor_nota):
    notas_mayor= []
    for x in cadena_nota:
        if x>=mayor_nota:
            notas_mayor.append(x) 
    print(f"La cantidad de notas mayores a {mayor_nota} es {len(notas_mayor)}")   
    return notas_mayor
        
def presente_nota (cadena_nota, actu_nota):
    notas_iguales= []
    for x in cadena_nota:
        if x==actu_nota:
            notas_iguales.append(x) 
    print(f"La cantidad de notas iguales a {actu_nota} es {len(notas_iguales)}")   
    return notas_iguales
    
            
            
while True:
    try:
        print("-"*30)
        print("Escoje una opcion")
        print("1. Nota aprobatoria")
        print("2. Agregar la lista de notas")
        print("3. Mirar por notas mayores")
        print("4. Mirar por notas iguales")
        print("5. Salir")
        print("-"*30)
        entrada = int(input("Tipea tu opcion: "))
        match entrada:
            case 1:
                print("Ingresa la nota actual")
                nota_actu = num_valido()
                print("Ahora la nota aprobatoria")
                nota_aprob = num_valido()
                aprob = aprobado(nota_actu, nota_aprob)
                if (aprob):
                    print("Aprobaste")
                else:
                    print("No aprobaste")
                    
            case 2:
                lista_notas = cadena_notas()
                print(f"El promedio de las notas es: {promedio_notas(lista_notas)}")
            case 3:
                if (lista_notas):
                    print("Ingresa la nota mayor")
                    nota_mayor = num_valido()
                    cadena_mayor = mayor_nota(lista_notas, nota_mayor)
                    print(f"Las notas mayores son: {cadena_mayor}")
                else:
                    print("No existe una lista de notas actualmente, usa la opcion 2")
            case 4:
                if (lista_notas):
                    print("Ingresa la nota a buscar sus repeticiones")
                    nota_igual = num_valido()
                    cadena_igual = presente_nota(lista_notas, nota_igual)
                else:
                    print("No existe una lista de notas actualmente, usa la opcion 2")
            case 5:
                sys.exit("Hasta la proxima")
            case _:
                print("Numero invalido")

    except ValueError:
        print("Tipeo invalido")
            
        
        
    

'''

'''
