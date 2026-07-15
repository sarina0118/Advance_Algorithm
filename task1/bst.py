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
            # Case 1: No child
            if node.left is None and node.right is None:
                return None

            # Case 2: One child
            elif node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            # Case 3: Two children
            successor = self._find_min(node.right)
            node.city = successor.city
            node.right = self._delete(node.right, successor.city.name)

        return node

    def _find_min(self, node):

        current = node

        while current.left is not None:
            current = current.left

        return current

    def height(self):
        return self._height(self.root)

    def _height(self, node):

        if node is None:
            return 0

        return 1 + max(
            self._height(node.left),
            self._height(node.right)
        )

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