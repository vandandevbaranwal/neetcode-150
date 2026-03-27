# Pattern: Stack — push operands, pop and compute on operator
# Trigger: "evaluate expression" = operators act on previous values = stack for order

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)    # order matters — b was pushed first
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))   # int(float()) handles truncation toward zero
            else:
                stack.append(int(c))   # operand — push to stack
        return stack[0]
    
    