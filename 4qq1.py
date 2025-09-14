class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
        self.size = size

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear == self.size - 1)

    def enqueue(self, item):
        if self.isFull():
            print("Queue is Full!")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = item

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            x = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front += 1
            print("Dequeued:", x)

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            print("Front Element:", self.queue[self.front])

    def display(self):
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            print("Queue Elements:", self.queue[self.front:self.rear+1])



q = Queue(5)
while True:
    print("\n1.Enqueue 2.Dequeue 3.Peek 4.Display 5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        val = int(input("Enter value: "))
        q.enqueue(val)
    elif ch == 2:
        q.dequeue()
    elif ch == 3:
        q.peek()
    elif ch == 4:
        q.display()
    else:
        break
