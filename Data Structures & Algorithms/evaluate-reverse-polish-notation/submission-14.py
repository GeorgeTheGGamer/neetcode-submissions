class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # O(n)

        stack = []
        
        for token in tokens:
            if token == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif token == "-":
                # Order matters here for negatives
                a,b = stack.pop() , stack.pop()
                stack.append(int(b) - int(a))
            elif token == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif token == "/":
                a, b = stack.pop() , stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(token))
        
        return stack[0]

