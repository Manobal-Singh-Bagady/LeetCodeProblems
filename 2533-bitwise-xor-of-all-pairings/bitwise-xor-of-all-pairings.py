class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        ans = 0
        if n1 & 1:
            for num in nums2:
                ans ^= num
        if n2 & 1:
            for num in nums1:
                ans ^= num
        return ans
        # if n1&1:
        #     if n2 & 1:
        #         ans = 0
        #         for i in nums2:
        #             ans ^= i
        #         for i in nums1:
        #             ans^=i
        #         return ans
        #     else:
        #         ans = 0
        #         for i in nums2:
        #             ans ^= i
        #         return ans
        # else:
        #     if n2 & 1:
        #         ans = 0
        #         for i in nums1:
        #             ans ^= i
        #         return ans
        #     else:
        #         return 0
