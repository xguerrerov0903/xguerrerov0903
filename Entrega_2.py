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
    

def aprovado (nota, aprobacion):
    if (nota>=aprobacion):
        return True
    else:
        return False

def mayor_nota (cadena_nota, mayor_nota):
    notas_mayor= []
    for x in cadena_nota:
        if x>=mayor_nota:
            notas_mayor.append(x) 
    return notas_mayor    
        
def presente_nota (cadena_nota, actu_nota):
    return 
    
    


