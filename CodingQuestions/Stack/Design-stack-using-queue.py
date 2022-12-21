from collections import deque
class MyStack:

    def __init__(self):
        self.Q1= deque()
        self.Q2= deque()

    def push(self, x: int) -> None:
        while len(self.Q1) > 0:
            self.Q2.append(self.Q1.popleft())
        self.Q1.append(x)
        while len(self.Q2) > 0:
            self.Q1.append(self.Q2.popleft())

    def pop(self) -> int:
        return self.Q1.popleft()

    def top(self) -> int:
        return self.Q1[0]

    def empty(self) -> bool:
        return len(self.Q1) == 0