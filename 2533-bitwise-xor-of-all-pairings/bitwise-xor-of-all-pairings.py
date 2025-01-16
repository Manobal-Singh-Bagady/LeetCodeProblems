class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        ans = 0
        if n1 & 1:
            for i in range(n2):
                ans ^= nums2[i]
        if n2 & 1:
            for i in range(n1):
                ans ^= nums1[i]
        return ans
