class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "}": "{", "]": "["}
        brackets = []
        for i in s:
            if i in "([{":
                brackets.append(i)
            else:
                if not brackets or brackets.pop() != bracket_map[i]:
                    return False
        return not brackets
