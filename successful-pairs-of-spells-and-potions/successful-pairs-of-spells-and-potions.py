import bisect
class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        s_potions = sorted(potions)
        ans = []
        for i in spells:
            if success % i == 0:
                neg = bisect.bisect_left(s_potions, (success)//i)
            else:
                neg = bisect.bisect_right(s_potions, (success)//i)
            ans.append(len(s_potions) - neg)
        return ans