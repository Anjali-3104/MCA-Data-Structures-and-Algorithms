
# Circular Queue

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Enqueue operation
    def enqueue(self, val):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = val
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = val

    # Dequeue operation
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.front == self.rear:
            print("Deleted element:", self.queue[self.front])
            self.front = -1
            self.rear = -1
        else:
            print("Deleted element:", self.queue[self.front])
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size

    # Display queue
    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            i = self.front
            while True:
                print(self.queue[i])
                if i == self.rear:
                    break
                i = (i + 1) % self.size

cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)

print("Circular Queue:")
cq.display()

cq.dequeue()

print("After deletion:")
cq.display()
