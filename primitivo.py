# Lista para almacenar los contactos
contactos = []

# Función para insertar un contacto
def insertar(nombre, telefono):
    if len(contactos) >= 5:
        print("No se pueden agregar más contactos.")
    else:
        contactos.append({"nombre": nombre, "telefono": telefono})

# Función para buscar un contacto
def buscar(nombre):
    for contacto in contactos:
        if contacto["nombre"] == nombre:
            return contacto["telefono"]
    return None

# Función para eliminar un contacto
def eliminar(nombre):
    global contactos
    for i, contacto in enumerate(contactos):
        if contacto["nombre"] == nombre:
            del contactos[i]
            print("Contacto eliminado.")
            return
    print("Contacto no encontrado.")

# Función para imprimir los contactos
def imprimir_contactos():
    if not contactos:
        print("No hay contactos.")
    else:
        for contacto in contactos:
            print(f"{contacto['nombre']} -> {contacto['telefono']}")

# Menú para interacción con el usuario
def menu():
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
            insertar(nombre, telefono)
        elif opcion == "2":
            nombre = input("Introduce el nombre del contacto a buscar: ")
            telefono = buscar(nombre)
            if telefono:
                print(f"El teléfono de {nombre} es {telefono}")
            else:
                print("Contacto no encontrado.")
        elif opcion == "3":
            nombre = input("Introduce el nombre del contacto a eliminar: ")
            eliminar(nombre)
        elif opcion == "4":
            imprimir_contactos()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# Ejecutar el menú
menu()
