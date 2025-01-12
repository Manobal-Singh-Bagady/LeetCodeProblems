class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if (n := len(s)) & 1:
            return False

        brackets = []
        unlocked = []

        for i in range(n):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                brackets.append(i)
            elif s[i] == ")":
                if brackets:
                    brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        while brackets and unlocked and brackets[-1] < unlocked[-1]:
            brackets.pop()
            unlocked.pop()

        return not brackets
