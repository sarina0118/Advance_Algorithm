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