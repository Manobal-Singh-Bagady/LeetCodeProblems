class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        greater = []
        equal = 0
        for i in nums:
            if i<pivot:
                less.append(i)
            elif i==pivot:
                equal+=1
            elif i>pivot:
                greater.append(i)
        ans = []
        ans += less
        ans += [pivot]*equal
        ans += greater
        return ans
        