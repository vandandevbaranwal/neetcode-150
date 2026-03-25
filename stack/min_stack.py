# Pattern: Two Stacks — auxiliary min stack tracks minimum at every state
# Trigger: "getMin in O(1)" = can't search = maintain parallel stack of minimums

class MinStack:
    def __init__(self):
        self.stack = []       # main stack
        self.minStack = []    # tracks minimum value at every level of main stack

    def push(self, val: int) -> None:
        self.stack.append(val)
        # minimum is either new val or current minimum — whichever is smaller
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()   # both stacks always stay in sync

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]  # current minimum always at top of minStack
    