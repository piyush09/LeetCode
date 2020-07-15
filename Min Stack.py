class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] # Initialising an empty list

    def push(self, x):
        self.stack.append(x) # Appending element x to stack

    def pop(self):
        return self.stack.pop() # Popping element from stack
        
    def top(self):
        return self.stack[-1] # Accessing last element of list stack - which is top of the stack
        
    def getMin(self):
        return min(self.stack) # Returning the minimum element of the stack


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print (obj.getMin())
print (obj.pop())
print (obj.top())
print (obj.getMin())