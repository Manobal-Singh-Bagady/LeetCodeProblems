class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        prefixSum = [0]
        count = 0
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                count += 1
            prefixSum.append(count)

        ans = []
        for s,e in queries:
            ans.append(prefixSum[e+1] - prefixSum[s])
        return ans
