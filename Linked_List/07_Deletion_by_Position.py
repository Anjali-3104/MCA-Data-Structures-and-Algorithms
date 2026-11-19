
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

    # Delete by position
    def del_position(self, pos):
        if self.head == None:
            print("List is empty")
        elif pos == 1:
            self.head = self.head.next
        else:
            temp = self.head
            i = 1
            while i < pos - 1 and temp:
                temp = temp.next
                i = i + 1

            if temp == None or temp.next == None:
                print("Invalid position")
            else:
                temp.next = temp.next.next

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

list.del_position(2)

list.print()
