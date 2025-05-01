import sys
sys.setrecursionlimit(10000)
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1

    def __repr__(self):
        return f'({self.data})'


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return AVLNode(value)

        if value < node.data:
            node.left_child = self._insert(node.left_child, value)
        elif value > node.data:
            node.right_child = self._insert(node.right_child, value)
        else:
            return node  # No se permiten duplicados

        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))
        balance = self.get_balance(node)

        # Rotaciones
        if balance > 1 and value < node.left_child.data:
            return self.rotate_right(node)
        if balance < -1 and value > node.right_child.data:
            return self.rotate_left(node)
        if balance > 1 and value > node.left_child.data:
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)
        if balance < -1 and value < node.right_child.data:
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)

        return node

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return node

        if value < node.data:
            node.left_child = self._delete(node.left_child, value)
        elif value > node.data:
            node.right_child = self._delete(node.right_child, value)
        else:
            if node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child
            temp = self.get_min(node.right_child)
            node.data = temp.data
            node.right_child = self._delete(node.right_child, temp.data)

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

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.data:
            return True
        elif key < node.data:
            return self._search(node.left_child, key)
        else:
            return self._search(node.right_child, key)

    def get_min(self, node):
        while node.left_child:
            node = node.left_child
        return node

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left_child) - self.get_height(node.right_child)

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
        if self.root:
            lines, *_ = self._build_tree_string(self.root)
            print("\n" + "\n".join((line.rstrip() for line in lines)))
        else:
            print("\nÁrbol vacío")

    def _build_tree_string(self, node):
        if node.right_child is None and node.left_child is None:
            line = str(node.data)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if node.right_child is None:
            lines, n, p, x = self._build_tree_string(node.left_child)
            s = str(node.data)
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if node.left_child is None:
            lines, n, p, x = self._build_tree_string(node.right_child)
            s = str(node.data)
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._build_tree_string(node.left_child)
        right, m, q, y = self._build_tree_string(node.right_child)
        s = str(node.data)
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
