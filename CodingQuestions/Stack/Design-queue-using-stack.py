class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if len(self.s2) > 0:
            return self.s2.pop()
        else:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
            return self.s2.pop()

    def peek(self) -> int:
        if len(self.s2) > 0:
            return self.s2[-1]
        else:
            return self.s1[0]

    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0