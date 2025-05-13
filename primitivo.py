# Variables globales para 5 contactos
nombre1 = telefono1 = ""
nombre2 = telefono2 = ""
nombre3 = telefono3 = ""
nombre4 = telefono4 = ""
nombre5 = telefono5 = ""

# Función para insertar un contacto
def insertar(nombre, telefono, contador):
    global nombre1, telefono1, nombre2, telefono2, nombre3, telefono3, nombre4, telefono4, nombre5, telefono5

    if contador == 0:
        nombre1, telefono1 = nombre, telefono
        contador += 1
    elif contador == 1:
        nombre2, telefono2 = nombre, telefono
        contador += 1
    elif contador == 2:
        nombre3, telefono3 = nombre, telefono
        contador += 1
    elif contador == 3:
        nombre4, telefono4 = nombre, telefono
        contador += 1
    elif contador == 4:
        nombre5, telefono5 = nombre, telefono
        contador += 1
    else:
        print("No se pueden agregar más contactos.")

    return contador

# Función para buscar un contacto
def buscar(nombre):
    if nombre1 == nombre:
        return telefono1
    elif nombre2 == nombre:
        return telefono2
    elif nombre3 == nombre:
        return telefono3
    elif nombre4 == nombre:
        return telefono4
    elif nombre5 == nombre:
        return telefono5
    else:
        return None

# Función para eliminar un contacto
def eliminar(nombre, contador):
    global nombre1, telefono1, nombre2, telefono2, nombre3, telefono3, nombre4, telefono4, nombre5, telefono5

    if nombre1 == nombre:
        nombre1, telefono1 = "", ""
        contador -= 1
    elif nombre2 == nombre:
        nombre2, telefono2 = "", ""
        contador -= 1
    elif nombre3 == nombre:
        nombre3, telefono3 = "", ""
        contador -= 1
    elif nombre4 == nombre:
        nombre4, telefono4 = "", ""
        contador -= 1
    elif nombre5 == nombre:
        nombre5, telefono5 = "", ""
        contador -= 1
    else:
        print("Contacto no encontrado.")
    
    return contador

# Función para ver todos los contactos
def imprimir_contactos():
    if nombre1 != "":
        print(f"{nombre1} -> {telefono1}")
    if nombre2 != "":
        print(f"{nombre2} -> {telefono2}")
    if nombre3 != "":
        print(f"{nombre3} -> {telefono3}")
    if nombre4 != "":
        print(f"{nombre4} -> {telefono4}")
    if nombre5 != "":
        print(f"{nombre5} -> {telefono5}")

# Menú principal
def menu():
    contador = 0
    while True:
        print("\n1. Insertar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Ver contactos")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Introduce el nombre del contacto: ")
            telefono = input("Introduce el teléfono del contacto: ")
            contador = insertar(nombre, telefono, contador)
        elif opcion == "2":
            nombre = input("Introduce el nombre del contacto a buscar: ")
            telefono = buscar(nombre)
            if telefono:
                print(f"El teléfono de {nombre} es {telefono}")
            else:
                print("Contacto no encontrado.")
        elif opcion == "3":
            nombre = input("Introduce el nombre del contacto a eliminar: ")
            contador = eliminar(nombre, contador)
        elif opcion == "4":
            imprimir_contactos()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# Ejecutar menú
menu()
