

class HashTable:
    def __init__(self):
        self.max_size = 10
        self.hash_table = [-1]*self.max_size

    def add(self, key, val):
        index = hash(key) % self.max_size
        if self.hash_table[index] == -1:
            self.hash_table[index] = [
                [key, val]
            ]
        else:
            updated = False
            for i in self.hash_table[index]:
                if i[0] == key:
                    i[1] = val
                    updated = True
            if not updated:
                self.hash_table[index].append([key, val])

    def remove(self, key):
        index = hash(key) % self.max_size
        if self.hash_table[index] == -1:
            return
        for idx, ele in enumerate(self.hash_table[index]):
            if ele[0] == key:
                del self.hash_table[index][idx]
                if not self.hash_table[index]:
                    self.hash_table[index] = -1

    def loopup(self, key):
        index = hash(key) % self.max_size
        if self.hash_table[index] == -1:
            return
        for ele in self.hash_table[index]:
            if ele[0] == key:
                return ele[1]


ht = HashTable()
print(ht.add("hari", 100))
print(ht.add("krishna", 200))
print(ht.add("name1", 300))
print(ht.add("name2", 220))
print(ht.add("name3", 222))
print(ht.add("name4", 200))
print(ht.add("name5", 200))
print(ht.add("name6", 200))
print(ht.hash_table)
print(ht.remove("name1"))
print(ht.loopup("name3"))
print(ht.hash_table)
