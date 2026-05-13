class MinStack:

    def __init__(self):
        #lets build using 2 stack
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        
        if val == self.minstack[-1]:
            self.minstack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
    

    def getMin(self) -> int:
        return self.minstack[-1]
        
