
# Singly Linear Linked List

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node

    # Insert at specific position
    def insert_position(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            i = 1
            while i < pos - 1 and temp:
                temp = temp.next
                i = i + 1

            if temp == None:
                print("Invalid position")
            else:
                new_node.next = temp.next
                temp.next = new_node

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

list = LinkedList()

list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))

list.insert_position(Node(25), 3)

list.print()
