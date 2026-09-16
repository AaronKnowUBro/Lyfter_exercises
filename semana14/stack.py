class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def print_stack(self):
        current = self.top
        output = ""
        while current is not None:
            output += str(current.data) + (" -> " if current.next is not None else "")
            current = current.next
        print(output if output != "" else "Stack is empty")


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.print_stack()

stack.pop()
stack.print_stack()