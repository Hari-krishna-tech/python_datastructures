class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.lenght = 0

    def size(self):
        return self.lenght

    def head(self):
        return self.head

    def add(self, val):
        node = Node(val)
        if self.head == None:
            self.lenght += 1
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        self.lenght += 1
        cur.next = node

    def remove(self, val):
        if self.head == None:
            return
        if self.head.val == val:
            self.lenght -= 1
            self.head = self.head.next
        cur = self.head
        pre = None
        while cur and cur.val != val:
            pre = cur
            cur = cur.next
        if cur:
            self.lenght -= 1
            pre.next = cur.next

    def isEmpty(self):
        return self.lenght == 0

    def indexOf(self, val):
        if self.head == None:
            return -1
        if self.head.val == val:
            return 0
        cur = self.head
        index = -1
        while cur and cur.val != val:
            index += 1
            cur = cur.next
        return index


ll = LinkedList()

ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.add(6)

print(ll.lenght)
