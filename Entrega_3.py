import sys
lista_productos = []

def cantidad_valido():
    cantidad = 0
    while True:
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
        for poscicion in range(len(lista_productos)):
            nombre_producto_actual = lista_productos[poscicion].get("Nombre",False)
            if (nombre_producto_actual.upper()==nombre_producto.upper()):
                return poscicion
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
        if existente is False:
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
                        nombre_producto = input("Ingresa el nombre del producto: \n")
                        if not nombre_producto:
                            print("El nombre no puede estar vacío\n")
                            continue                       
                        poscicion_producto = comprobacion_existencia(nombre_producto)
                        if not poscicion_producto:
                            print("Producto no existente")
                            break
                        else:
                            print(f"Nombre: {lista_productos[poscicion_producto]["Nombre"]}")
                            print(f"Precio: {lista_productos[poscicion_producto]["Precio"]}$ | Cantidad: {lista_productos[poscicion_producto]["Cantidad"]}")
                            break
                else: 
                    print("*"*20)
                    print("No existen productos en el inventario")
                    print("*"*20)
            case 3:
                if lista_productos:
                    while True:
                            nombre_producto = input("Ingresa el nombre del producto: \n")
                            if not nombre_producto:
                                print("El nombre no puede estar vacío\n")
                                continue      
                            poscicion_producto = comprobacion_existencia(nombre_producto)
                            if poscicion_producto is False:
                                print("Producto no existente")
                                break
                            else:
                                nuevo_precio = precio_valido()
                                lista_productos[poscicion_producto]["Precio"] = nuevo_precio
                                print("La nueva informacion de tu producto es:")
                                print(f'Nombre: {lista_productos[poscicion_producto]["Nombre"]}')
                                print(f'Precio: {lista_productos[poscicion_producto]["Precio"]}$ | Cantidad: {lista_productos[poscicion_producto]["Cantidad"]}')
                else:
                    print("*"*20)
                    print("No existen productos en el inventario")
                    print("*"*20)
            case 4:
                if (lista_productos):
                    while True:
                        nombre_producto = input("Ingresa el nombre del producto: \n")
                        if not nombre_producto:
                            print("El nombre no puede estar vacío\n")
                            continue                       
                        poscicion_producto = comprobacion_existencia(nombre_producto)
                        if poscicion_producto is False:
                            print("Producto no existente")
                            break
                        else:
                            lista_productos.pop(poscicion_producto)
                            print(f"Eliminacion exitosa de {nombre_producto}")
            case 5:
                if (lista_productos):
                    print(lista_productos)
                    total_inventario = list(map(lambda x: x["Precio"] * x["Cantidad"], lista_productos))
                    sum_inventario = sum(total_inventario)
                    print(f"El total es {sum_inventario}$")

                else:
                    print("*"*20)
                    print("No existen productos en el inventario")
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
