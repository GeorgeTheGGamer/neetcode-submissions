class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        # Add to the minstack only if this value is less than or equal
        if (self.minStack and val <= self.minStack[-1]) or not(self.minStack):
            self.minStack.append(val)
        self.stack.append(val)
        
        

    def pop(self) -> None:

        value = self.stack.pop()
        # Must pop this value from minStack to hold the global minimum value
        if value == self.minStack[-1]:
            self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # min is O(n), must be O(1)
        return self.minStack[-1]
        
