

class PriorityQueue:
    def __init__(self):
        self.priority_queue = []
        self.count = 0

    def values(self):
        return self.priority_queue

    def isEmpty(self):
        return self.count == 0

    def front(self):
        if not self.isEmpty():
            return self.priority_queue[0]

    def dequeue(self):
        if not self.isEmpty():
            self.count -= 1
            self.priority_queue.pop(0)
            return True
        return False

    def enqueue(self, val):
        if self.isEmpty():
            self.count += 1
            self.priority_queue.append(val)
            return
        added = False
        for i in range(self.count):
            if val[1] < self.priority_queue[i][1]:
                self.count += 1
                self.priority_queue.insert(i, val)
                added = True
        if not added:
            self.priority_queue.append(val)


pq = PriorityQueue()

pq.enqueue(["value1", 2])
pq.enqueue(["value2", 1])
pq.enqueue(["value3", 3])
pq.enqueue(["value4", 1])

print(pq.values())
