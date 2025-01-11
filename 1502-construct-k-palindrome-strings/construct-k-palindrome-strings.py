class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k == len(s):
            return True
        if k>len(s):
            return False
        map = dict()
        for char in s:
            map[char] = map.get(char,0)+1
        
        if sum(1 for i in map if map[i]%2!=0)>k:
            return False
        else:
            return True
        

        