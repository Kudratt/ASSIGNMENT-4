from collections import deque

class Stack2Q:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1:
            return "Stack Empty"
        return self.q1.popleft()

    def top(self):
        return self.q1[0] if self.q1 else "Empty"

    def display(self):
        print("Stack:", list(self.q1))

# Example
s = Stack2Q()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Popped:", s.pop())
s.display()
class Stack1Q:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):  
            self.q.append(self.q.popleft())

    def pop(self):
        if not self.q:
            return "Stack Empty"
        return self.q.popleft()

    def top(self):
        return self.q[0] if self.q else "Empty"

    def display(self):
        print("Stack:", list(self.q))

# Example
s = Stack1Q()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Popped:", s.pop())
s.display()
class Stack1Q:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):  
            self.q.append(self.q.popleft())

    def pop(self):
        if not self.q:
            return "Stack Empty"
        return self.q.popleft()

    def top(self):
        return self.q[0] if self.q else "Empty"

    def display(self):
        print("Stack:", list(self.q))

# Example
s = Stack1Q()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Popped:", s.pop())
s.display()
