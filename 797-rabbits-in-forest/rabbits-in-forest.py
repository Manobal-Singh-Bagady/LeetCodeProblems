class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for others in count:
            group_size = others +1
            num_groups = math.ceil(count[others]/group_size)
            ans += num_groups * group_size
        return ans