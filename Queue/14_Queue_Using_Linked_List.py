
# Queue Using Linked List

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue operation
    def enqueue(self, new_node):
        if self.rear == None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # Dequeue operation
    def dequeue(self):
        if self.front == None:
            print("Queue is empty")
        else:
            temp = self.front
            print("Deleted element:", temp.data)
            self.front = self.front.next

            if self.front == None:
                self.rear = None

    # Display queue
    def display(self):
        if self.front == None:
            print("Queue is empty")
        else:
            temp = self.front
            while temp:
                print(temp.data)
                temp = temp.next

queue = Queue()

queue.enqueue(Node(10))
queue.enqueue(Node(20))
queue.enqueue(Node(30))
queue.enqueue(Node(40))

print("Queue elements:")
queue.display()

queue.dequeue()

print("After deletion:")
queue.display()
