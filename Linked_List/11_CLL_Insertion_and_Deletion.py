
# Circular Linked List

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
            new_node.next = self.head
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # Insert at beginning
    def insert_begin(self, new_node):
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

    # Delete from beginning
    def del_begin(self):
        if self.head == None:
            print("List is empty")
        elif self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            self.head = self.head.next
            temp.next = self.head

    # Delete from end
    def del_end(self):
        if self.head == None:
            print("List is empty")
        elif self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while(temp.next.next != self.head):
                temp = temp.next
            temp.next = self.head

    def print(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while True:
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break

list = LinkedList()

list.append(Node(10))
list.append(Node(20))
list.append(Node(30))

list.insert_begin(Node(5))
list.del_end()

list.print()
