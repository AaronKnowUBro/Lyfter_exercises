class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            raise IndexError("pop from empty deque")
        popped_data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return popped_data

    def pop_right(self):
        if self.tail is None:
            raise IndexError("pop from empty deque")
        popped_data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return popped_data

    def print_deque(self):
        current = self.head
        output = ""
        while current is not None:
            output += str(current.data) + (" <-> " if current.next is not None else "")
            current = current.next
        print(output if output != "" else "Deque is empty")


deque = Deque()
deque.push_right(10)
deque.push_right(20)
deque.push_left(5)
deque.print_deque()

deque.pop_left()
deque.print_deque()

deque.pop_right()
deque.print_deque()