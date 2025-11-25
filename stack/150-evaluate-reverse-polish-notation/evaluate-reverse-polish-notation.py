class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]

        for ch in tokens:
            if ch == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
                
            elif ch =="-":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second) - int(first))
                
            elif ch =="*":
                stack.append(int(stack.pop()) * int(stack.pop()))
                
            elif ch =="/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second) / int(first))
                
            else:
                stack.append(ch)
                
        return int(stack[-1])