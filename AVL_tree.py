import sys
sys.setrecursionlimit(10000)

class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.clave = [ord(c.upper()) for c in nombre]  # Clave para ordenar (ASCII)

    def __lt__(self, other):
        return self.clave < other.clave

    def __gt__(self, other):
        return self.clave > other.clave

    def __eq__(self, other):
        return self.clave == other.clave

    def __repr__(self):
        return f"{self.nombre} -> {self.telefono}"


class AVLNode:
    def __init__(self, contacto):
        self.data = contacto
        self.left_child = None
        self.right_child = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, contacto):
        self.root = self._insert(self.root, contacto)

    def _insert(self, node, contacto):
        if node is None:
            return AVLNode(contacto)

        if contacto < node.data:
            node.left_child = self._insert(node.left_child, contacto)
        elif contacto > node.data:
            node.right_child = self._insert(node.right_child, contacto)
        else:
            return node  # Contacto duplicado

        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))
        balance = self.get_balance(node)

        if balance > 1 and contacto < node.left_child.data:
            return self.rotate_right(node)
        if balance < -1 and contacto > node.right_child.data:
            return self.rotate_left(node)
        if balance > 1 and contacto > node.left_child.data:
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)
        if balance < -1 and contacto < node.right_child.data:
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)

        return node

    def search(self, nombre):
        clave = [ord(c.upper()) for c in nombre]
        return self._search(self.root, clave)

    def _search(self, node, clave):
        if node is None:
            return None
        if clave == node.data.clave:
            return node.data
        elif clave < node.data.clave:
            return self._search(node.left_child, clave)
        else:
            return self._search(node.right_child, clave)

    def delete(self, nombre):
        clave = [ord(c.upper()) for c in nombre]
        self.root = self._delete(self.root, clave)

    def _delete(self, node, clave):
        if node is None:
            return node

        if clave < node.data.clave:
            node.left_child = self._delete(node.left_child, clave)
        elif clave > node.data.clave:
            node.right_child = self._delete(node.right_child, clave)
        else:
            if node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child
            temp = self.get_min(node.right_child)
            node.data = temp.data
            node.right_child = self._delete(node.right_child, temp.data.clave)

        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left_child) >= 0:
            return self.rotate_right(node)
        if balance > 1 and self.get_balance(node.left_child) < 0:
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)
        if balance < -1 and self.get_balance(node.right_child) <= 0:
            return self.rotate_left(node)
        if balance < -1 and self.get_balance(node.right_child) > 0:
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)

        return node

    def llamar(self, nombre):
        contacto = self.search(nombre)
        if contacto:
            print(f"Llamando a {contacto.nombre}: {contacto.telefono}")
        else:
            print("Contacto no encontrado.")

    def get_min(self, node):
        while node.left_child:
            node = node.left_child
        return node

    def get_height(self, node):
        return 0 if node is None else node.height

    def get_balance(self, node):
        return self.get_height(node.left_child) - self.get_height(node.right_child) if node else 0

    def rotate_left(self, z):
        y = z.right_child
        T2 = y.left_child
        y.left_child = z
        z.right_child = T2
        z.height = 1 + max(self.get_height(z.left_child), self.get_height(z.right_child))
        y.height = 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))
        return y

    def rotate_right(self, z):
        y = z.left_child
        T3 = y.right_child
        y.right_child = z
        z.left_child = T3
        z.height = 1 + max(self.get_height(z.left_child), self.get_height(z.right_child))
        y.height = 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))
        return y

    def print_pretty(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left_child)
            print(f"{node.data.nombre} -> {node.data.telefono}")
            self._inorder(node.right_child)
