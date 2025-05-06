'''
Implementación de la Solución:
Entrada de datos:
Solicita al usuario los datos necesarios para cada operación (nombre del producto, precio, cantidad), y valida que los datos entren limpios
Si estás solicitando un número y el usuario ingresa una letra, en lugar de arrojar una excepción debes mostrar una notificación adecuada
Funciones: Crea funciones que implementen cada funcionalidad del programa:
Añadir producto (con parámetros para nombre, precio y cantidad) XXXX
Buscar producto por nombre (con retorno de precio y cantidad)
Actualizar precio (función que recibe el nombre del producto y el nuevo precio)
Eliminar producto (recibe el nombre del producto)
Calcular el valor total del inventario con una función lambda
Colecciones:
Usa una lista con diccionarios en su interior para almacenar los productos
'''
import sys
lista_productos = []

def cantidad_valido():
    cantidad = 0
    try:
        while cantidad <= 0 or cantidad % 1 != 0:
            cantidad = float(input("Ingresa la cantidad de tu producto: \n"))
            if (cantidad <= 0 or cantidad % 1 != 0):
                print("Cantidad invalido, ingreso un valor positivo y entero")
    except ValueError:
        print("Ingresa caracteres numericos unicamente")
    cantidad = int(cantidad)
    return cantidad
            
def precio_valido():
    precio = 0.0
    try:
            while precio < 0:
                precio = float(input("Ingresa el precio de tu producto: \n"))
                if (precio < 0):
                    print("Precio invalido, ingreso un valor positivo")
    except ValueError:
            print("Ingresa caracteres numericos unicamente")
    precio = round(precio, 2)
    return precio
    
            
def comprobacion_existencia (nombre_producto):
    if (lista_productos):
        for producto in lista_productos:
            nombre_producto_actual = producto.get("Nombre",False)
            if (nombre_producto_actual.upper()==nombre_producto.upper()):
                return producto
        return False
    else:   
        return False



def agregar_producto ():    
    producto = {
        "Nombre" : "",
        "Precio" : 0.0,
        "Cantidad" : 0
    }
    while True:
        nombre_producto = input("Ingresa el nombre de tu producto: \n")
        existente = comprobacion_existencia(nombre_producto.upper())
        if not nombre_producto:
            print("El nombre no puede estar vacío\n")
            continue
        if (existente):
            print("Producto ya existente \n")
            continue
        else:
            producto["Nombre"] = nombre_producto
        
        precio = precio_valido()
        producto["Precio"] = precio
        
        cantidad = cantidad_valido()
        producto["Cantidad"] = cantidad
        
        lista_productos.append(producto)
        



while True:
    try:
        print("-"*30)
        print('''
              
              ¿Que opcion deseas escoger?
              
                1. Añadir producto
                2. Buscar producto
                3. Actualizar precio
                4. Eliminar producto
                5. Calcular el valor total del inventario
                6. Salir
                
            ''')
        print("-"*30)
        entrada = int(input("Tipea tu opcion: "))
        match entrada:
            case 1:
                agregar_producto()
            case 2:
                if lista_productos:
                    while True:
                        nombre_producto = input("Ingresa el nombre de tu producto: \n")
                        if not nombre_producto:
                            print("El nombre no puede estar vacío\n")
                            continue
                        break
                    diccionario_producto = comprobacion_existencia(nombre_producto)
                    if not diccionario_producto:
                        print("Producto no existente")
                    else:
                        print(f"Precio: {diccionario_producto["Precio"]} | Cantidad: {diccionario_producto["Cantidad"]}")
            case 3:
                # Debes cambiar la funcion comprobacion_existencia, esto dado que no la podras reutilizar en este caso, por lo tanto necesitaras
                # que te regrese la posicion y no el diccionario
                if (lista_productos):
                    print("Ingresa la nota mayor")
            case 4:
                if (lista_productos):
                    print("Ingresa la nota a buscar sus repeticiones")
            case 5:
                if (lista_productos):
                    print(lista_productos)
                else:
                    print("*"*20)
                    print("No existe una lista de notas actualmente, usa la opcion 2")
                    print("*"*20)
            case 6:
                print("*"*20)
                sys.exit("Hasta la proxima")
            case _:
                print("Numero invalido")
    except ValueError:
        print("*"*20)
        print("[TIPEO INVALIDO]")
        print("*"*20)
