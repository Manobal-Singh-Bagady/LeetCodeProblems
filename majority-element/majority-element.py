class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Hashing

        # mp = {}
        # for i in nums:
        #     if i not in mp:
        #         mp[i]=1
        #     else:
        #         mp[i]+=1
        # N = len(nums)
        # for x,y in mp.items():
        #     if y>N/2:
        #         return x

        # Moor's Algorithm

        el = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                count += 1
                el = nums[i]
            elif el == nums[i]:
                count +=1
            else:
                count -=1
        return el