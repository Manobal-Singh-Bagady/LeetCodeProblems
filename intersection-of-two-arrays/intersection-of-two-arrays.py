class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        ans = []
        n = len(nums1)
        m = len(nums2)
        while i<n and j<m:
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                if len(ans)==0 or ans[-1]!=nums1[i]:
                    ans.append(nums1[i])
                i+=1
                j+=1
        return ans