class Set:
    def __init__(self):
        self.set = {}
        self.count = 0

    def has(self, val):
        return val in self.set

    def values(self):
        values = []
        for i in self.set:
            values.append(i)
        return values

    def add(self, val):
        if self.has(val):
            return False
        self.count += 1
        self.set[val] = 1
        return True

    def remove(self, val):
        if self.has(val):
            self.count -= 1
            del self.set[val]
            return True
        return False

    def size(self):
        return self.count

    def union(self, otherSet):
        union = Set()
        for i in self.set:
            union.add(i)
        for i in otherSet:
            union.add(i)
        return union

    def intersection(self, otherSet):
        intersection = Set()
        for i in self.set:
            if otherSet.has(i):
                intersection.add(i)
        return intersection

    def difference(self, otherSet):
        difference = Set()
        for i in self.set:
            if not otherSet.has(i):
                difference.add(i)
        return difference

    def isSubset(self, subset):
        for i in subset:
            if not self.set.has(i):
                return False
        return True


mySet = Set()
mySet.add(1)
mySet.add(2)
mySet.add(3)
mySet.add(4)
mySet.add(5)
mySet.add(6)
mySet.add(7)
mySet.remove(4)
mySet.remove(6)
print(mySet.size())
print(mySet.has(5))
print(mySet.has(6))
print(mySet.values())
