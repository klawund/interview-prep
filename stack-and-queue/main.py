class Stack:
    def __init__(self):
        self.elements = []
        self.pointer = -1
    
    def push(self, item):
        self.pointer += 1
        self.elements.insert(self.pointer, item)
    
    def pop(self):
        item = self.elements[self.pointer]
        self.pointer -= 1

        return item

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

# print(stack.pop()) # 3
# print(stack.pop()) # 2

stack.push(4)

# print(stack.pop()) # 4
# print(stack.pop()) # 1

class Queue:
    def __init__(self):
        self.elements = []
        self.head = 0
        self.tail = 0
    
    # when implementing with an actual array, the array can be circular so that when it fills up and the head has increased,
    # the head pointer can go back to the beggining
    def push(self, item):
        self.elements.insert(self.tail, item)
        self.tail += 1

    def pop(self):
        item = self.elements[self.head]
        self.head += 1

        return item
    
queue = Queue()

queue.push(1)
queue.push(2)
queue.push(3)

# print(queue.pop()) # 1
# print(queue.pop()) # 2

queue.push(4)

# print(queue.pop()) # 3
# print(queue.pop()) # 4