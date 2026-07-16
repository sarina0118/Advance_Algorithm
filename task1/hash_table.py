class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, city):
        index = self.hash_function(city.name)
        self.table[index].append(city)

    def search(self, name):
        index = self.hash_function(name)
        for city in self.table[index]:
            if city.name == name:
                return city
        return None
    
    def delete(self, name):
        index = self.hash_function(name)
        for i, city in enumerate(self.table[index]):
            if city.name == name:
                del self.table[index][i]
                return True
        return False
    
    def display(self):
        for bucket in self.table:
            for city in bucket:
                print(city)
                print("-" * 40)

    def count(self):
        total = 0
        for bucket in self.table:
            total += len(bucket)
        return total
    
    