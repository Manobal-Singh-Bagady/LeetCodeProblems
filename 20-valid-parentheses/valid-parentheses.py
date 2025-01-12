class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        for i in s:
            if i=='(' or i=='[' or i=='{':
                brackets.append(i)
            elif i==')':
                if brackets and brackets[-1]=='(':
                    brackets.pop()
                else:
                    return False
            elif i=='}':
                if brackets and brackets[-1]=='{':
                    brackets.pop()
                else:
                    return False
            elif i==']':
                if brackets and brackets[-1]=='[':
                    brackets.pop()
                else:
                    return False
        if brackets:
            return False
        return True
        