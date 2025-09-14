class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
        self.size = size

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.isFull():
            print("Queue is Full!")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            x = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
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
            i = self.front
            print("Queue Elements:", end=" ")
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()



cq = CircularQueue(5)
while True:
    print("\n1.Enqueue 2.Dequeue 3.Peek 4.Display 5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        val = int(input("Enter value: "))
        cq.enqueue(val)
    elif ch == 2:
        cq.dequeue()
    elif ch == 3:
        cq.peek()
    elif ch == 4:
        cq.display()
    else:
        break
