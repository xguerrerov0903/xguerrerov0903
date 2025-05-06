import sys

# Lista global que contiene los productos del inventario.
lista_productos = []

# Función que valida la cantidad de un producto. Debe ser un número entero positivo.
def cantidad_valido():
    while True:
        try:
            cantidad = int(input("Ingresa la cantidad de tu producto: \n"))
            if cantidad <= 0:
                print("Cantidad inválida, ingresa un valor entero positivo.")  # Valida que la cantidad sea mayor que cero
            else:
                return cantidad  # Devuelve la cantidad válida
        except ValueError:
            print("Ingresa caracteres numéricos únicamente.")  # En caso de que no sea un número

# Función que valida el precio de un producto. Debe ser un número flotante mayor que cero.
def precio_valido():
    while True:
        try:
            precio = float(input("Ingresa el precio de tu producto: \n"))
            if (precio <= 0):  # Valida que el precio sea mayor que cero
                print("Precio invalido, ingreso un valor positivo")
                continue
        except ValueError:
            print("Ingresa caracteres numericos unicamente")  # En caso de que no sea un número
            continue
        precio = round(precio, 2)  # Redondea el precio a dos decimales
        return precio  # Devuelve el precio válido

# Función que verifica si un producto ya existe en el inventario (basado en el nombre).
def comprobacion_existencia(nombre_producto):
    if (lista_productos):  # Si la lista de productos no está vacía
        for poscicion in range(len(lista_productos)):  # Recorre la lista de productos
            nombre_producto_actual = lista_productos[poscicion].get("Nombre", False)  # Obtiene el nombre del producto actual
            if (nombre_producto_actual.upper().strip() == nombre_producto.upper().strip()):  # Compara sin considerar mayúsculas ni espacios
                return poscicion  # Devuelve la posición del producto si ya existe
        return False  # Si no encuentra el producto, devuelve False
    else:
        return False  # Si la lista está vacía, devuelve False

# Función que agrega un nuevo producto al inventario
def agregar_producto():
    producto = {
        "Nombre": "",
        "Precio": 0.0,
        "Cantidad": 0
    }
    while True:
        nombre_producto = input("Ingresa el nombre de tu producto: \n")  # Solicita el nombre del producto
        existente = comprobacion_existencia(nombre_producto)  # Verifica si el producto ya existe en el inventario
        if not nombre_producto:  # Si el nombre del producto está vacío
            print("El nombre no puede estar vacío\n")
            continue
        if not existente is False:  # Si el producto ya existe
            print("Producto ya existente \n")
            continue
        else:
            producto["Nombre"] = nombre_producto  # Asigna el nombre al producto
        
        precio = precio_valido()  # Solicita y valida el precio del producto
        producto["Precio"] = precio
        
        cantidad = cantidad_valido()  # Solicita y valida la cantidad del producto
        producto["Cantidad"] = cantidad
        
        lista_productos.append(producto)  # Agrega el producto a la lista
        break  # Sale del bucle una vez que el producto ha sido agregado

# Bucle principal donde el usuario selecciona las opciones del menú
while True:
    try:
        # Menú de opciones para el usuario
        print("-" * 30)
        print('''
              
              ¿Qué opción deseas escoger?
              
                1. Añadir producto
                2. Buscar producto
                3. Actualizar precio
                4. Eliminar producto
                5. Calcular el valor total del inventario
                6. Salir
                
            ''')
        print("-" * 30)
        entrada = int(input("Tipea tu opcion: "))  # Solicita al usuario que ingrese una opción
        match entrada:
            case 1:
                agregar_producto()  # Llama a la función para agregar un producto
            case 2:
                if lista_productos:  # Si la lista de productos no está vacía
                    while True:
                        nombre_producto = input("Ingresa el nombre del producto: \n")  # Solicita el nombre del producto a buscar
                        if not nombre_producto:  # Si el nombre está vacío
                            print("El nombre no puede estar vacío\n")
                            continue
                        poscicion_producto = comprobacion_existencia(nombre_producto)  # Busca el producto en el inventario
                        if poscicion_producto is False:  # Si no encuentra el producto
                            print("Producto no existente")
                            break
                        else:
                            # Si encuentra el producto, muestra la información
                            print(f'Nombre: {lista_productos[poscicion_producto]["Nombre"]}')
                            print(f'Precio: {lista_productos[poscicion_producto]["Precio"]}$ | Cantidad: {lista_productos[poscicion_producto]["Cantidad"]}')
                            break
                else:
                    print("*" * 20)
                    print("No existen productos en el inventario")  # Si no hay productos en el inventario
                    print("*" * 20)
            case 3:
                if lista_productos:  # Si la lista de productos no está vacía
                    while True:
                        nombre_producto = input("Ingresa el nombre del producto: \n")  # Solicita el nombre del producto a actualizar
                        if not nombre_producto:  # Si el nombre está vacío
                            print("El nombre no puede estar vacío\n")
                            continue
                        poscicion_producto = comprobacion_existencia(nombre_producto)  # Busca el producto
                        if poscicion_producto is False:  # Si no encuentra el producto
                            print("Producto no existente")
                            break
                        else:
                            nuevo_precio = precio_valido()  # Solicita un nuevo precio para el producto
                            lista_productos[poscicion_producto]["Precio"] = nuevo_precio  # Actualiza el precio del producto
                            # Muestra la información actualizada del producto
                            print("La nueva información de tu producto es:")
                            print(f'Nombre: {lista_productos[poscicion_producto]["Nombre"]}')
                            print(f'Precio: {lista_productos[poscicion_producto]["Precio"]}$ | Cantidad: {lista_productos[poscicion_producto]["Cantidad"]}')
                            break
                else:
                    print("*" * 20)
                    print("No existen productos en el inventario")  # Si no hay productos en el inventario
                    print("*" * 20)
            case 4:
                if lista_productos:  # Si la lista de productos no está vacía
                    while True:
                        nombre_producto = input("Ingresa el nombre del producto: \n")  # Solicita el nombre del producto a eliminar
                        if not nombre_producto:  # Si el nombre está vacío
                            print("El nombre no puede estar vacío\n")
                            continue
                        poscicion_producto = comprobacion_existencia(nombre_producto)  # Busca el producto
                        if poscicion_producto is False:  # Si no encuentra el producto
                            print("Producto no existente")
                            break
                        else:
                            lista_productos.pop(poscicion_producto)  # Elimina el producto de la lista
                            print(f"Eliminación exitosa de {nombre_producto}")
                            break
            case 5:
                if lista_productos:  # Si la lista de productos no está vacía
                    total_inventario = list(map(lambda x: x["Precio"] * x["Cantidad"], lista_productos))  # Calcula el total por cada producto
                    sum_inventario = sum(total_inventario)  # Suma el total de todos los productos
                    print(f"El total es {sum_inventario}$")  # Muestra el valor total del inventario
                else:
                    print("*" * 20)
                    print("No existen productos en el inventario")  # Si no hay productos en el inventario
                    print("*" * 20)
            case 6:
                print("*" * 20)
                sys.exit("Hasta la próxima")  # Sale del programa
            case _:
                print("Número inválido")  # Si el usuario ingresa una opción inválida
    except ValueError:
        print("*" * 20)
        print("[TIPEO INVALIDO]")  # Si el usuario ingresa algo que no es un número en una opción
        print("*" * 20)
