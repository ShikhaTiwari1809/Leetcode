class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack =[]
        final_sum = 0
        if operations[0]=="C" or operations[0]=="D" or operations[0]=="+" or operations[1]=="+":
            return 0
        for ch in operations:
            if ch =="C":
                final_sum-=stack[-1]
                stack.pop()
            elif ch =="D":
                stack.append(int(stack[-1])*2)
                final_sum+=stack[-1]
            elif ch =="+":
                stack.append(int(stack[-1])+int(stack[-2]))
                final_sum+=stack[-1]
            else :
                stack.append(int(ch))
                final_sum+=stack[-1]
            
         
        return final_sum
