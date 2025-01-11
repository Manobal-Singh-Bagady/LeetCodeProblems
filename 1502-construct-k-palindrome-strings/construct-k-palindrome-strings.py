class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        map = Counter(s)
        odds = 0
        for i in map.values():
            if i%2:
                odds+=1
        return odds<=k and k<=len(s)
        # n = len(s)
        # if k == n:
        #     return True
        # if k > n:
        #     return False

        # odds = 0
        # for i in set(s):
        #     if s.count(i) % 2:
        #         odds += 1

        # if odds <= k:
        #     return True
        # return False
