class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        temp = 0
        for i in accounts:
            t = sum(i)
            if t >= temp:
                temp = t
        return temp