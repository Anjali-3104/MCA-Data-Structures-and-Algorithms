
# Stack Using Linked List

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    # Pop operation
    def pop(self):
        if self.top == None:
            print("Stack is empty")
        else:
            temp = self.top
            print("Deleted element:", temp.data)
            self.top = self.top.next
            temp.next = None

    # Peek operation
    def peek(self):
        if self.top == None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    # Display stack
    def display(self):
        if self.top == None:
            print("Stack is empty")
        else:
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

stack = Stack()

stack.push(Node(10))
stack.push(Node(20))
stack.push(Node(30))

print("Stack elements:")
stack.display()

stack.peek()

stack.pop()

print("After pop:")
stack.display()
