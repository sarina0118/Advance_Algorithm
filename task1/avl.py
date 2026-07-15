from city import City


class AVLNode:
    def __init__(self, city):
        self.city = city
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def update_height(self, node):
        node.height = 1 + max(
            self.get_height(node.left),
            self.get_height(node.right)
        )

    def right_rotate(self, y):
        x = y.left
        t2 = x.right
        x.right = y
        y.left = t2
        self.update_height(y)
        self.update_height(x)
        return x

    def left_rotate(self, x):
        y = x.right
        t2 = y.left
        y.left = x
        x.right = t2
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, city):
        self.root = self._insert(self.root, city)

    def _insert(self, node, city):
        if node is None:
            return AVLNode(city)
        if city.name < node.city.name:
            node.left = self._insert(node.left, city)
        elif city.name > node.city.name:
            node.right = self._insert(node.right, city)
        else:
            return node
        self.update_height(node)
        balance = self.get_balance(node)
        if balance > 1 and city.name < node.left.city.name:
            return self.right_rotate(node)
        if balance < -1 and city.name > node.right.city.name:
            return self.left_rotate(node)
        if balance > 1 and city.name > node.left.city.name:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and city.name < node.right.city.name:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def search(self, name):
        return self._search(self.root, name)
    
    def _search(self, node, name):
        if node is None:
            return None
        if node.city.name == name:
            return node.city
        if name < node.city.name:
            return self._search(node.left, name)
        return self._search(node.right, name)
    
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.city)
            print("-" * 40)
            self._inorder(node.right)

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, name):
        self.root = self._delete(self.root, name)

    def _delete(self, node, name):

        if node is None:
            return node

        if name < node.city.name:
            node.left = self._delete(node.left, name)

        elif name > node.city.name:
            node.right = self._delete(node.right, name)

        else:

            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            successor = self.find_min(node.right)

            node.city = successor.city

            node.right = self._delete(node.right, successor.city.name)

        self.update_height(node)

        balance = self.get_balance(node)
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def count_nodes(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, node):

        if node is None:
            return 0

        return (
            1
            + self._count_nodes(node.left)
            + self._count_nodes(node.right)
        )

    def height(self):
        return self.get_height(self.root)