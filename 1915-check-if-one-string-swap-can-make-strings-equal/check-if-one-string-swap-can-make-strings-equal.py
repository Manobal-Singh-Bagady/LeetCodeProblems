class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        
        first_char = -1
        second_char = -1
        diff = 0        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
                if first_char==-1 and second_char==-1:
                    first_char=s1[i]
                    second_char=s2[i]
                elif first_char!=s2[i] or second_char!=s1[i]:
                    return False
            if diff>2:
                return False
        
        if s1==-1 or s2==-1 or diff == 1:
            return False
        return True
