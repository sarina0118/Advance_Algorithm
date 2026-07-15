from city import City
from bst import BinarySearchTree
from avl import AVLTree

tree = BinarySearchTree()
tree.insert(City("Kathmandu", 85.32, 27.71, 845767, 12.5))
tree.insert(City("Pokhara", 83.99, 28.20, 402995, 30.1))
tree.insert(City("Butwal", 83.45, 27.70, 195054, 18.2))
tree.insert(City("Biratnagar", 87.27, 26.45, 244750, 22.3))
tree.insert(City("Dharan", 87.28, 26.81, 153875, 16.8))

print("Cities in Alphabetical Order\n")
tree.inorder()
print("\nSearching for Pokhara...\n")
result = tree.search("Pokhara")
if result:
    print(result)
else:
    print("City not found.")
print("\nTotal Cities:", tree.count_nodes())
print("Tree Height:", tree.height())
print("\nDeleting Butwal city from list\n")
tree.delete("Butwal")
print("Cities after deletion:\n")
tree.inorder()
print("\nTotal Cities:", tree.count_nodes())

tree = AVLTree()
tree.insert(City("Kathmandu", 85.32, 27.71, 845767, 12.5))
tree.insert(City("Pokhara", 83.99, 28.20, 402995, 30.1))
tree.insert(City("Butwal", 83.45, 27.70, 195054, 18.2))
tree.insert(City("Biratnagar", 87.27, 26.45, 244750, 22.3))
tree.insert(City("Dharan", 87.28, 26.81, 153875, 16.8))

print("Cities in AVL Tree (Alphabetical Order)\n")
tree.inorder()
print("\nSearching for Kathmandu...\n")
result = tree.search("Kathmandu")
if result:
    print(result)
else:
    print("City not found.")