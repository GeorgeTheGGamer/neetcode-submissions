class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # O(n)

        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b-a))
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))      # No floor needed 
            else:
                stack.append(int(token))    # Only need for int since we are pushing integers to the stack
        return stack[0]
    
            


