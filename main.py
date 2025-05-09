from AVL_tree import AVLTree, Contacto

def menu_de_contactos():
    tree = AVLTree()

    while True:
        print("\n--- ADMINISTRADOR DE CONTACTOS ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Llamar a contacto")
        print("5. Mostrar contactos (ordenados)")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre del contacto: ")
            telefono = input("Número de teléfono: ")
            tree.insert(Contacto(nombre, telefono))
            print("Contacto agregado.")

        elif opcion == '2':
            nombre = input("Nombre a buscar: ")
            encontrado = tree.search(nombre)
            print(f"{encontrado.nombre} -> {encontrado.telefono}" if encontrado else "No encontrado.")

        elif opcion == '3':
            nombre = input("Nombre del contacto a eliminar: ")
            tree.delete(nombre)
            print("Contacto eliminado (si existía).")

        elif opcion == '4':
            nombre = input("¿A quién quieres llamar?: ")
            tree.llamar(nombre)

        elif opcion == '5':
            print("Lista de contactos:")
            tree.print_pretty()

        elif opcion == '6':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida.")   
        
