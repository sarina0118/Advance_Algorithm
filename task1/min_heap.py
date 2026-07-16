from city import City

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, city):
        self.heap.append(city)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index].distance < self.heap[parent].distance:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index]
                )
                index = parent
            else:
                break

    def remove_min(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return root
    
    def heapify_down(self, index):

        size = len(self.heap)

        while True:

            smallest = index

            left = 2 * index + 1
            right = 2 * index + 2

            if (
                left < size
                and self.heap[left].distance < self.heap[smallest].distance
            ):
                smallest = left

            if (
                right < size
                and self.heap[right].distance < self.heap[smallest].distance
            ):
                smallest = right

            if smallest != index:

                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index]
                )

                index = smallest

            else:
                break

    def display(self):
        if len(self.heap) == 0:
            print("Heap is empty.")
            return

        for city in self.heap:
            print(city)
            print("-" * 40)

    def size(self):
        return len(self.heap)