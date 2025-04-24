# 1.1
print()
nombre= input("¡Hey tu! Dime tu nombre: ")
print()
edad= input("Psssssss y tu edad: ")

print("Hola "+edad+" tienes "+nombre+" años :)")

# 1.2
print()
comida= input("Tu comida favorita es... ")
print()
color= input("Y tu color favorito es...  ")

print(f"Entonces {comida} y {color} muy basico")

# 1.3
print()
numero1= float(input("Dime un numero "))
numero2= numero1*2
numero3= numero1*3

print(f"Tu numero es {numero1}, el cual su doble es {numero2} y su tiple {numero3}")

#2.1

var_scrip= "Scrip"

var_int= 123

var_float= 123.45

var_boolean= False

#2.2
var_float_c= 123.00

var_change_int= int(var_float_c)

#2.3

var_stri_int = float(input("Dime un numero "))

var_stri_int_2= var_stri_int*2

print(var_stri_int_2)

#2.4

def true_number (string_number):
    
    try:
        number_from_string = int(string_number)
        return True
        
    except ValueError:
        return False
    
#3.1

print()
base= float(input("Base del rectangulo "))
print()
altura= float(input("Altura del rectangulo "))

area= base*altura

print(f"El area es {area}")

#3.2 precio * (1 - descuento / 100)

print()
precio_total= float(input("¿Cual es el precio? "))
print()
descuento= float(input("¿Cual es el descuento? "))

precio_descuento = precio_total * (1 - descuento / 100)


print(f"El precio final es {precio_descuento}")

#3.3

print()
div_numero_1= int(input("Dime tu primer numero "))
print()
div_numero_2= int(input("Dime tu segundo numero numero "))

div_resudio= div_numero_1%div_numero_2

print(f"El residuo es {div_resudio}")

#3.4

test_operadores = 2+4*8/13-6

print(f"El residuo es {test_operadores}")

#4.1

print()
bool_numero_1= float(input("Dime tu primer numero "))
print()
bool_numero_2= float(input("Dime tu segundo numero "))

if bool_numero_1>bool_numero_2:
    print(f"{bool_numero_1} es mayor")

elif bool_numero_2>bool_numero_1:
    print(f"{bool_numero_2} es mayor")
else:
    print("Son iguales")

#4.2

print()
bool_edad= int(input("Dime tu edad  "))

if bool_edad>=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edads")
    
#4.3

bool_string_1= input("Dime un texto ")
print()
bool_string_2= input("Dime otro texto ")

if bool_string_1==bool_string_2:
    print("Positivo para plagio")
else:
    print("Continua")

#5.1


print()
bool_edad_1= int(input("Dime tu edad  "))
print()
licencia= True

while True:
    bool_licencia= input("¿Tienes licencia?(Si o No)  ").upper()
    if (bool_licencia=="SI"):
        break
    elif(bool_licencia=="NO"):
        licencia= False
        break   
    print("Respuesta invalida")

if bool_edad>=18:
    licencia= False
    
if licencia:
    print("Puedes conducir")
else:
    print("No puedes conducir")

#5.2

trabajo= True

while True:
    bool_exp= input("¿Tienes experiencia laboral?(Si o No)  ").upper()
    if (bool_exp=="SI"):
        break
    elif(bool_exp=="NO"):
        trabajo= False
        break   
    print("Respuesta invalida")
    
while True:
    bool_titulo= input("¿Tienes titulo universitario?(Si o No)  ").upper()
    if (bool_titulo=="SI"):
        break
    elif(bool_titulo=="NO"):
        trabajo= False
        break   
    print("Respuesta invalida")
    
if trabajo:
    print("Puedes trabajar")
else:
    print("No puedes trabajar")
    
#5.3

print()
bool_num_range= int(input("Dime un numero  "))

if(10<=bool_num_range<=50):
    print("Esta en el rango de 10 a 50")
else:
    print("No esta en el rango de 10 a 50")