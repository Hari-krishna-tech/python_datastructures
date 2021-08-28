
class Queue:
    def __init__(self):
        self.queue = []
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def enqueue(self, val):
        self.queue.append(val)
        self.count += 1

    def front(self):
        if not self.isEmpty():
            return self.queue[0]

    def dequeue(self):
        if self.isEmpty():
            return
        self.count -= 1
        return self.queue.pop(0)

    def size(self):
        return self.count


"""
stack: list : append, pop  /O(1)
queue: list : append, pop(0) /O(1)

"""

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q.front())
q.dequeue()
print(q.front())
