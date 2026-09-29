class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        # 1 2 

        # stack 5

        # 5
        # 9-4
        # 3 3 * 
        # 1 + 2 

        stack = []

        for t in tokens:
            if t == "+":
                a = stack.pop() 
                b = stack.pop()
                stack.append(a + b)
            
            elif t == "*":
                a = stack.pop() 
                b = stack.pop()
                stack.append(a * b)

            elif t == "-":
                a = stack.pop() 
                b = stack.pop()
                stack.append(b-a)

            elif t == "/":
                a = stack.pop() 
                b = stack.pop()
                stack.append(int(b / a))

            else:
                stack.append(int(t))
                
        return stack[0] 
        