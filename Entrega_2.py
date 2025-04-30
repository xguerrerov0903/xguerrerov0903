# Liberia  importada para el uso de sys.exit
import sys

# Funcion para el ingreso de notas validas
def num_valido ():
    # No se sale de la solicitud hasta tipear una opcion valida
    while True:
        try:
            nota = float(input("Ingresa la nota (0 a 100): "))
            # Dado que buscamos se ingrese una nota el tipeo valido sera un numero igual o mayor a 0 y menor o igual a 100
            if nota>=0 and nota<=100:
                # Cumplido el requisito se regreso al valor numerico tipeado y dado este es un return no se necesita del break para salir del while
                # ya que el return acaba con toda la funcion
                return nota
            else:
                print("Valor invalido")
        # En caso de intento de ingreso de un caracter no numerico saltara error pero se volvera a realizar la solicitud
        except ValueError:
            print("Valor invalido")

# Dado una nota (notas) correspondiente a una variable numerica y aprobacion (aprobacion) tambien una variable numerica se determina si aprueba o no
def aprobado (nota, aprobacion):
    # La forma de comprobacion es mirando si la nota es mayor o igual a la aprobacion regresando asi True o False de acuerdo a esto
    if (nota>=aprobacion):
        return True
    else:
        return False

# Esta funcion le corresponde armar una lista de notas con la entrada de texto del usuario revisando que todo sea cumplido sin problemas
def cadena_notas ():
    # Esta funcion no saldra hasta tener una lista de notas valida
    while True:
        try:
            entrada = input("Ingresa tus notas separados por comas (0 al 100): ")
            # Creamos una lista vacia la cual se ira llenando con las notas entregadas
            valores = []
            # Como se indico la entreda seran notas separadas por comas "," por eso mismo se realiza un split cada que se encuentre con uno de estos elementos
            for x in entrada.split(","):
                # Se confirma que las notas ingresadas sean validas (0 al 100) ademas de convertirlas a un nunmero float
                if 0 <= float(x.strip()) <= 100:
                    # Si esta se cumple con normalidad las notas seras agregadas a la lista valores
                    valores.append(float(x.strip()))
                else:
                    # En caso del tipeo de una nota invalidad se indicara esto y se volvera a realizar la solicitud
                    raise ValueError("Notas fuera de rango")               
            break
        # En caso de que se tipeo un caracter diferente a numeros, comas y espacios en blanco saltara error y se entregara el mensaje            
        except ValueError:
            print("Cadena de valores invalida")
    # La funcion regresara una lista con las notas que se hayan tipeado
    return valores      

# Esta funcion entregara el promedio de una lista de notas (lista_notas)
def promedio_notas (lista_notas):
    suma_notas = 0
    # En principio hace una suma de todas las notas de la lista con la funcion for que recorre esta lista
    for x in lista_notas:
        suma_notas += x
    # Y luego esta suma de notas la divide por el numero total de elementos de la lista, osea de notas
    # Regresando asi el promedio
    # Usamos la funcion len para conocer la longitud de la lista por lo tanto la cantidad de notas existentes
    return suma_notas/len(lista_notas)

# Con esta funcion determino que notas y cuantos son mayores o iguales de una lista de notas (cadena_nota) de acuerdo a una nota especifica (mayor_nota)
def mayor_nota (cadena_nota, mayor_nota):
    # En inicio creo una lista vacia donde pondre las notas mayores o igual a
    notas_mayor= []
    # Recorro los elemento de la lista de notas que me proporcionaron
    for x in cadena_nota:
        # Evaluo elemento por elemento cual es mayor a la nota especifica
        if x>=mayor_nota:
            # De serlo lo agrero a mi lista de notas mayores
            notas_mayor.append(x) 
    # Dado que me lista si cuente con elemento imprimire el mensaje que indica cuantas notas son mayores o igual a la nota especifica
    # Es bueno aclarar que el if se cumple si la lista no esta vacia, ya que de estar vacia seria False
    if (notas_mayor):
        # Usamos la funcion len para conocer la longitud de la lista y asi reconocer la cantidad de elementos que son mayores o igules
        print(f"La cantidad de notas mayores a {mayor_nota} es {len(notas_mayor)}")   
        # Retorno la cadena con las notas 
        return notas_mayor
    else:
        # Aun cuando sea vacia la retorna para salir de la funcion
        return notas_mayor

# Con esta funcion determino que notas y cuantos son iguales de una lista de notas (cadena_nota) de acuerdo a una nota especifica (actu_nota)       
def presente_nota (cadena_nota, actu_nota):
    # En inicio creo una lista vacia donde pondre las notas igual al a nota especifica
    notas_iguales= []
    # Recorro los elemento de la lista de notas que me proporcionaron
    for x in cadena_nota:
        # Evaluo elemento por elemento cual es igual a la nota especifica
        if x==actu_nota:
            # De serlo lo agrero a mi lista de notas iguales
            notas_iguales.append(x) 
    # Dado que me lista si cuente con elemento imprimire el mensaje que indica cuantas notas igual a la nota especifica
    if (notas_iguales):
        # Usamos la funcion len para conocer la longitud de la lista y asi reconocer la cantidad de elementos que son iguales
        print(f"La cantidad de notas iguales a {actu_nota} es {len(notas_iguales)}")   
    # De estar vacia entonces me indicara que no hay notas iguales a la nota especifica
    else: 
        print(f"No hay notas iguales a {actu_nota}")  
    
#Creo una lista vacia para las notas           
lista_notas= []            

# Empiezo un while que funcionara para desplegar mi menu 
while True:
    # El try se encargara de soportar tipeo de caracteres que no sean los esperados (numericos enteros)
    try:
        # Imprimo el menu con sus opciones a escoger
        print("-"*30)
        print("Escoje una opcion")
        print("1. Nota aprobatoria")
        print("2. Agregar la lista de notas")
        print("3. Mirar por notas mayores")
        print("4. Mirar por notas iguales")
        print("5. Mirar lista actual de notas")
        print("6. Salir")
        print("-"*30)
        # Ingreso de la opcion de menu deseada
        entrada = int(input("Tipea tu opcion: "))
        # Se evalua que opcion se ingreso
        match entrada:
            # Cuando se solicita de opcion 1 de nota aprovatoria se solicita la nota actual (nota_actu) y que nota seria la aprobotaria (nota_aprob)
            case 1:
                print("Ingresa la nota actual")
                # Se comprueba que sea una nota valida solicitandola con la funcion num_valido()
                nota_actu = num_valido()
                print("Ahora la nota aprobatoria")
                # Igualmente aqui
                nota_aprob = num_valido()
                # Se llama la funcion aprobado() ingresando la nota actual y la aprobatoria para validar la aprovacion
                aprob = aprobado(nota_actu, nota_aprob)
                # De acuerdo al resultado booleano entregado por la funcion aprobado se imprime "Aprobaste" en caso de True o "No aprobaste" en caso de False
                if (aprob):
                    print("*"*20)
                    print("Aprobaste")
                    print("*"*20)
                else:
                    print("*"*20)
                    print("No aprobaste")
                    print("*"*20)
            # Cuando se escoja la opcion 2 para agregar  una lista de notas se llama la funcion cadena_notas para este proceso y despues la funcion promedio_notas()
            case 2:
                # Se crea la lista de notas (lista_notas) con la funcion cadena_notas() la cual se encargara de que se cree una lista correcta comprobando
                # una entreda correcta de los datos
                lista_notas = cadena_notas()
                # Despues se imprime el promedio de estas notas con la funcion promedio_notas() entregandole la lista realizada previamente
                print(f"El promedio de las notas es: {promedio_notas(lista_notas)}")
            # En el caso del llamado de la opcion 3 del menu primero se comprueba si hay una lista existente de notas para trabajar con ella en caso de no existir lanza
            # un mensaje indicando esto mismo y que opcion del menu se debe usar para tener una lista
            case 3:
                # Se comprueba la existencia de la lista
                if (lista_notas):
                    print("Ingresa la nota mayor")
                    # Solicito la nota mayor especifica (nota_mayor) con la funcion num_valido() para comprobar que sea un tipeo valido
                    nota_mayor = num_valido() 
                    # Con esta nota y la lista de notas (lista_notas) llamo a la funcion mayor_nota que se encargara que buscar por la notaqs iguales mayor 
                    cadena_mayor = mayor_nota(lista_notas, nota_mayor)
                    # De acuerdo a si la lista que optenga sea vacia o no imprimo el mensaje correspondiente
                    if (cadena_mayor):                        
                        print(f"Las notas mayores son: {cadena_mayor}")
                    else:
                        print(f"No hay notas mayores a {nota_mayor}")
                # Aqui se imprime el mensaje de "error" para el caso que se haga llamado de la opcion del menu sin una lista de notas aun
                else:
                    print("*"*20)
                    print("No existe una lista de notas actualmente, usa la opcion 2")
                    print("*"*20)
            # En el caso del llamado de la opcion 4 del menu primero se comprueba si hay una lista existente de notas para trabajar con ella en caso de no existir lanza
            # un mensaje indicando esto mismo y que opcion del menu se debe usar para tener una lista
            case 4:
                if (lista_notas):
                    print("Ingresa la nota a buscar sus repeticiones")
                    # Solicito la nota igual especifica (nota_igual) con la funcion num_valido() para comprobar que sea un tipeo valido
                    nota_igual = num_valido()
                    # Llamo la funcion entregandole la lista de notas (lista_notas) y la nota igual a comprar para ya este encargarse de imprimir
                    # el mensaje correspondiente
                    presente_nota(lista_notas, nota_igual)  
                # Aqui se imprime el mensaje de "error" para el caso que se haga llamado de la opcion del menu sin una lista de notas aun                   
                else:
                    print("*"*20)
                    print("No existe una lista de notas actualmente, usa la opcion 2")
                    print("*"*20)
            # Para el llamado de la opcion 5 simplemente se imprimira la lista o no si esta existe
            case 5:
                # En caso de no tener una lista vacia (True) imprimo la lista actual
                if (lista_notas):
                    print(lista_notas)
                # En caso contrario se imprime el mensaje de "error" para el caso que se haga llamado de la opcion del menu sin una lista de notas aun      
                else:
                    print("*"*20)
                    print("No existe una lista de notas actualmente, usa la opcion 2")
                    print("*"*20)
            case 6:
                print("*"*20)
                sys.exit("Hasta la proxima")
            # En caso de un tipeo numerico entero que no se encuentre en las opciones salta error
            case _:
                print("Numero invalido")
    # Entrega el mensaje de error en caso de tipeo erroneo
    except ValueError:
        print("*"*20)
        print("[TIPEO INVALIDO]")
        print("*"*20)
            
            
