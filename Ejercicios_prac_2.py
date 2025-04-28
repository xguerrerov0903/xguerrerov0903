import random

# 1

while True:
    try:
        num_entero= int(input("Dame un numero que yo hago magia "))
        break
    except ValueError:
        print("Ingresa un valor numerico y ENTERO ")
if(num_entero>0):
    print(f"{num_entero} es positivo")
elif (num_entero<0):
    print(f"{num_entero} es negativo")
else:
    print(f"{num_entero} es cero")

# 2
# Yo lei que le dieran varias calificaciones y de ahi sacar el promedio :(

calificacion = 0
num_calificacion = 0

while True:  
    while True:
        try:
            nota = float(input("Ingresa tu nota (0 a 100): "))
            if nota>=0 and nota<=100:
                calificacion += nota
                num_calificacion += 1
                break
            else:
                print("Valor invalido")
        except ValueError:
            print("Valor invalido")
    while True:
        continua= input("Ingresaras mas notas (Si o No): ").upper()
        if (continua=="SI"):
            break
        elif(continua=="NO"):
            break
        else:
            print("Respuesta no valida")  
    if(continua=="NO"):
            break  
    
promedi = calificacion/num_calificacion

if (promedi>=60):
    print(f"Aprobaste con: {promedi}")
else:
    print(f"No aprobaste con: {promedi}")

#3

while True:
    try:
        num_mul= float(input("Dame un numero que yo hago magia ;D "))
        break
    except ValueError:
        print("Ingresa un valor numerico")

for i in range(10):
    print(f"{num_mul}x{i+1} = {num_mul*(i+1)}")

# 4

while True:
    try:
        while True:
            num_positivo= int(input("Dame un numero que yo hago la cuenta atras "))
            if num_positivo>=0:
                break
            else:
                print("Ingresa un numero positivo")
        break
    except ValueError:
        print("Ingresa un valor numerico y ENTERO ")

while num_positivo != -1:
    print(num_positivo)
    num_positivo = num_positivo-1

# 5

num_aleatorio = random.randint(1, 10)
num_intento = 0


while num_intento<=3:
    while True:
        try:
            while True:
                num_advina= int(input("Adivina el numero (1 al 10): "))
                if num_advina >0 and num_advina < 11:
                    break
                else:
                    print("El numero no se encuentra en el rango")
            break
        except ValueError:
            print("Ingresa un valor numerico y ENTERO ")
    if (num_advina==num_aleatorio):
        print(f"Acertaste el numero: {num_aleatorio}")
        break
    elif (num_advina>num_aleatorio):
        print(f"Tu numero {num_advina} es mayor al numero")
    else:
        print(f"Tu numero {num_advina} es menor al numero")
    num_intento += 1
    if num_intento<3:
        print(f"Tienes {3-num_intento} mas")
    else:
        print(f"Te quedaste sin intentos perdiste. El numero es {num_aleatorio}")
    






