class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        closing_mapping = {')':'(',
        '}':'{',
        ']':'['}

        characters = list(s)
       
        for ch in characters:
            if ch in closing_mapping.values():
                stack.append(ch)
            else:
                if len(stack)==0:
                    return False
                if stack[-1]!=closing_mapping[ch]:
                    return False
                stack.pop()
            
          
       
        return len(stack) == 0
        