class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if (n := len(s)) & 1:
            return False

        brackets = 0
        unlocked = 0

        for i in range(n):
            if locked[i] == "0":
                unlocked+=1
            elif s[i] == "(":
                brackets+=1
            elif s[i] == ")":
                if brackets:
                    brackets-=1
                elif unlocked:
                    unlocked-=1
                else:
                    return False

        balance = 0
        for i in range(n-1, -1, -1):
            if locked[i]=='0':
                balance -=1
                unlocked-=1
            elif s[i]=='(':
                balance+=1
                brackets-=1
            elif s[i]==')':
                balance-=1

            if balance>0:
                return False
            if unlocked==0 and brackets==0:
                return True
        # while brackets and unlocked and brackets[-1] < unlocked[-1]:
        #     brackets.pop()
        #     unlocked.pop()

        if brackets>0:
            return False
        return True
