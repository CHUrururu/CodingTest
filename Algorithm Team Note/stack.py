class Stack:
    def __init__(self, size = 10000):
        self.arr = [None] * size
        self.last_index = 0
    
    def push(self, value):
        self.arr[self.last_index] = value
        self.last_index += 1

    def pop(self):
        if (self.empty()):
            raise Exception('stack is empty.')
        self.last_index -= 1
        return self.arr[self.last_index]

    def empty(self):
        if (self.last_index == 0):
            return True
        else:
            return False

    def peek(self):
        if (self.empty()):
            raise Exception('stack is empty.')
        return self.arr[self.last_index - 1]
