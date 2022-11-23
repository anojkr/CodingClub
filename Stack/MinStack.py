"""
    Logic:
        setup two stack
            minStack
            stack
        push() ->
            stack.push(item),
            if len(minStack) == 0 or minStack.top() >= item
                minStack.push(item)

        pop() ->
            if len(stack) > 0:
                topVal = stack.pop()
                if len(minStack) > 0 and minStack[-1] == topVal:
                    minStack.pop()
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            topVal = self.stack.pop()
            if len(self.minStack) > 0 and self.minStack[-1] == topVal:
                self.minStack.pop()
            return topVal
        return -1

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minStack) > 0:
            return self.minStack[-1]
        return -1

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()