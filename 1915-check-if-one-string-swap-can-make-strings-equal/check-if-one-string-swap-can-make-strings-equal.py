class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        chars = []
        diff = 0
        for i in range(n):
            if s1[i] != s2[i]:
                diff+=1
                if not chars:
                    chars.append(s1[i])
                    chars.append(s2[i])
                else:
                    if chars[0]!=s2[i] or chars[1]!=s1[i]:
                        return False
        if len(chars)>2:
            return False
        if diff==2 or diff==0:
            return True
        return False
        