class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        num_indexes = defaultdict(list)
        ans = 0

        for i in range(len(nums)):
            for j in num_indexes[nums[i]]:
                if i*j%k==0:
                    ans+=1
            num_indexes[nums[i]].append(i)
        return ans
