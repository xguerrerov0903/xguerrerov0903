# Texto decorativo
print("="*30)
print("||  Validador de productos  ||")
print("="*30)  


# Inicio de mi lista carrito que contendra listas de producto con las variables [nombres, precio, cantidad, descuento]
carrito = []

# Funcion encargada de comprobar que el descuento ingresado se encuentre en el rango valido 0 al 100
def num_descuento():
    descuento = -10.00
# El while se encarga de no dejar salir usuario hasta el ingreso de un descuento valido, mientras el try de prevenir
# por si el usuario trata de agregar un caracter no numerico
    try:
        while descuento<0 or descuento>100:
            descuento= float(input("Ingresa el descuento de tu producto (0 a 100): \n"))
            if (descuento<0 or descuento>100):
                print("Descuento invalido, ingresa un descuento en el rango de 0 a 100")
        return descuento
    except ValueError:
        print("Ingresa caracteres numericos unicamente")

# El while se encarga de crear mi carrito permitiendo agregar tantos productos como el usuario desee
while True:
# Creo mi lista producto desde cero cada que repito mi bucle
    producto = []
    nombre= input("Ingresa el nombre de tu producto: \n")
# Agrego el nombre a mi lista producto
    producto.append(nombre)
    precio= -1.00
    # Un while encargado de comprobar que el precio ingresado sea positivo y el try previene error
    # por si el usuario trata de agregar un caracter no numerico
    try:       
        while precio < 0:
            precio= float(input("Ingresa el precio de tu producto: \n"))
            if (precio<0):
                print("Precio invalido, ingreso un valor positivo")
    except ValueError:
        print("Ingresa caracteres numericos unicamente")
# Limitamos los decimales a 2 y agregamos el precio a la lista producto
    precio = round(precio  , 2)  
    producto.append(precio)
    
    cantidad= -1.1
    
    try:
    # Un while encargado de comprobar que la cantidad  ingresada en mayor y diferente a cero y un numero intero y el try previene error
    # por si el usuario trata de agregar un caracter no numerico
        while cantidad<=0 or cantidad%1 != 0:
            # Se acepta un float para permitir mas facilmente los errores pero tambien se puede ver las alternativa de try
            # en esta seccion y el reto pero no se ha visto en los temas aprendidos en la semana 1
            cantidad= float(input("Ingresa la cantidad de tu producto: \n"))
            if (cantidad<=0 or cantidad%1 != 0):
                print("Cantidad invalido, ingreso un valor positivo y entero")
    except ValueError:
        print("Ingresa caracteres numericos unicamente")
# Se asigna como un int y se agrega a la lista la cantidad
    cantidad = int(cantidad)
    producto.append(cantidad)
    
# Se pregunta si existe un descuento o no y se asigna como upper para procesar las alternativas de mayusculas y minusculas
    yn_descuento= input("Tendra descuento (Si o No): \n").upper()
    descuento = -10.00
    
# Se evalua la respuesrta dada    
    if yn_descuento == "SI":
        # En caso de ser si se entre a la funcion num_descuento vista mas arriba
        descuento= round(num_descuento(),2)
    elif yn_descuento == "NO":
        # Si no se asigna descuento como 0
        descuento = 0
    else:
        # El while se encargada de repetir el ingreso de la pregunta hasta optener una respuesta valida
        while True:
            print("Respuesta invalidad, ingresa una respuesta validad")
            yn_descuento= input("Tendra descuento (Si o No): \n").upper()
            if yn_descuento == "SI":
                descuento= round(num_descuento(),2)
                break
            elif yn_descuento == "NO":
                descuento= 0.00
                break
            
    # Se agrega el descuento a la lista producto
    producto.append(descuento)
            
    

    # Se inicia un while del que no se saldra hasta tener una respuesta valida 
    while True:
        # Se realiza la pregunta de si se desea agregar mas productos
        mas_productos = input("¿Ingresaras mas producto? (Si o No)\n").upper()
        # Se comprueba las respuestas dadas 
        if (mas_productos=="SI"):
            # Se agrega la lista producto al carrito en ambos casos de si o no
            carrito.append(producto) 
            # Se rompe en while en ambos casos al ser una respuesta valida
            break
        elif(mas_productos=="NO"):
            carrito.append(producto)
            break      
    if (mas_productos=="NO"):
        # Se rompe el while en caso de no para dejar de agregar productos
        carrito.append(producto)
        break


# Facturacion   
   
# Texto decorativo     
print("")
print("")
print("")
print("="*30)
print("||\t  Factura\t  ||")
print("="*30)  
print("")
print("_"*30)       
print("") 
print("-" * 35)
subtotal = 0
total= 0
# Se inicio un for que recorrera los elementos del carrito en este caso las listas productos
for i in carrito:
    # Se imprime de la listas teniendo en cuenta este orden [nombres, precio, cantidad, descuento]
    print(f"{i[0]}\t{i[1]}$\t{i[2]}\t{i[1]*i[2]}$")
    # En caso de que el descuento sea mayor a 0 se aplicara este descuento y se sumera el total del producto 
    # con el descuento
    if i[3]>0:
        subtotal= round((i[1]*i[2])-(((i[1]*i[2])*(i[3])*0.01)))
        print(f"\tPrecio con descuente del {i[3]}%, es de {subtotal}")
    else:
        subtotal= (i[1]*i[2])
    print("-" * 35)
    # Antes de iniciar un nuevo ciclo for se suma el subtotal del producto en que se encuentra el codigo en 
    # el momento al total completo de la compra
    total= total+subtotal
print(f"Tu total es: {total}$")

