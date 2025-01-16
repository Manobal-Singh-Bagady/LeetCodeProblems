class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        if n1&1:
            if n2 & 1:
                ans = 0
                for i in nums2:
                    ans ^= i
                for i in nums1:
                    ans^=i
                return ans
            else:
                ans = 0
                for i in nums2:
                    ans ^= i
                return ans
        else:
            if n2 & 1:
                ans = 0
                for i in nums1:
                    ans ^= i
                return ans
            else:
                return 0
