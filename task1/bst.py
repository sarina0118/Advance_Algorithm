from city import City


class BSTNode:
    def __init__(self, city):
        self.city = city
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, city):
        if self.root is None:
            self.root = BSTNode(city)
        else:
            self._insert(self.root, city)

    def _insert(self, node, city):

        if city.name < node.city.name:

            if node.left is None:
                node.left = BSTNode(city)
            else:
                self._insert(node.left, city)

        elif city.name > node.city.name:

            if node.right is None:
                node.right = BSTNode(city)
            else:
                self._insert(node.right, city)

    def search(self, name):
        return self._search(self.root, name)

    def _search(self, node, name):

        if node is None:
            return None

        if node.city.name == name:
            return node.city

        elif name < node.city.name:
            return self._search(node.left, name)

        else:
            return self._search(node.right, name)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):

        if node:

            self._inorder(node.left)

            print(node.city)

            print("-" * 40)

            self._inorder(node.right)