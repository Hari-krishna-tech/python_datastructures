"""
visualization 
https://www.cs.usfca.edu/~galles/visualization/Heap.html

"""


class MinHeap:
    def __init__(self):

        self.heap_list = [0]
        self.current_size = 0

    def sift_up(self, i):
        """
        Moves the value up in the tree to maintain the heap property.
        """
        while i // 2 > 0:

            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i //
                                                  2] = self.heap_list[i // 2], self.heap_list[i]

            i = i // 2

    def insert(self, k):
        """
        Inserts a value into the heap
        """
        self.heap_list.append(k)
        self.current_size += 1
        self.sift_up(self.current_size)

    def sift_down(self, i):

        while (i * 2) <= self.current_size:

            mc = self.min_child(i)

            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):

        if (i * 2)+1 > self.current_size:
            return i * 2
        else:

            if self.heap_list[i*2] < self.heap_list[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1

    def delete_min(self):

        if len(self.heap_list) == 1:
            return 'Empty heap'

        root = self.heap_list[1]

        self.heap_list[1] = self.heap_list[self.current_size]

        self.heap_list.pop()

        self.current_size -= 1

        self.sift_down(1)

        return root

    def heap_sort(self):
        sorted_list = []
        while self.current_size > 0:
            sorted_list.append(self.delete_min())
        print(sorted_list)


my_heap = MinHeap()
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(7)
my_heap.insert(9)
my_heap.insert(13)
my_heap.insert(11)
my_heap.insert(10)
my_heap.heap_sort()
print(my_heap.delete_min())
