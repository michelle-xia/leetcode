class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        val = self.stack[-1]
        del self.stack[-1]
        return val

    def top(self):
        return self.stack[-1]

    def getMin(self):
        if len(self.stack) > 0:
            minval = self.stack[0]
            for i in range(1, len(self.stack)):
                if self.stack[i] < minval:
                    minval = self.stack[i]
            return minval


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()