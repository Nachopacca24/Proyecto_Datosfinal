from AVL_tree import AVLTree


def menu_de_contactos():
    tree=AVLTree()

    while True:
        print("\n--- ADMINISTRADOR DE CONTACTOS (solo teléfonos) ---")
        print("1. Agregar número")
        print("2. Buscar número")
        print("3. Eliminar número")
        print("4. Mostrar árbol AVL")
        print("5. Salir")
        opcion = int (input("Elige una opción: "))

        if opcion==1:
            try:
                numero_telefono = int (input("Ingresa el numero de telefono aa gregar: "))
                tree.insert(numero_telefono)
                print("numero de telefono agregado")
            except ValueError:
                print("Número inválido.")
            
        elif opcion==2: 
            try:
                num = int(input("Número de teléfono a buscar: "))
                encontrado = tree.search(num)
                print("Número encontrado." if encontrado else "Número no encontrado.")
            except ValueError:
                print("Número inválido.")

        if opcion==3:
            try:
                num = int(input("Número de teléfono a eliminar: "))
                tree.delete(num)
                print("Número eliminado.")
            except ValueError:
                print("Número inválido.")

        elif opcion==4:
            tree.print_pretty()

        elif opcion == 5:
            print("Saliendo del administrador de contactos.")
            break     
        