class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for e in s:
            if e in ('(', '[', '{'):
                stack.append(e)
            else:
                if not stack:
                    return False 
                if stack[-1] == '(' and e != ')':
                    return False
                if stack[-1] == '{' and e != '}':
                    return False
                if stack[-1] == '[' and e != ']':
                    return False
                temp = stack.pop() 
        
        return not stack