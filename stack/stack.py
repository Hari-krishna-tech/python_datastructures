

class Stack:
    def __init__(self):
        self.stack = {}
        self.count = 0

    def push(self, val):
        self.stack[self.count] = val
        self.count += 1

    def pop(self):
        if self.count == 0:
            return
        self.count -= 1
        val = self.stack[self.count]
        del self.stack[self.count]
        return val

    def peek(self):
        if self.count == 0:
            return
        return self.stack[self.count-1]

    def length(self):
        return self.count

    def __str__(self):
        ans = ""
        for i in range(self.count):
            ans += str(self.stack[i]) + " "
        return ans


stack = Stack()

stack.push(1)
print(stack.peek())
stack.push(2)
print(stack.peek())

print(stack.length())

print(stack)
