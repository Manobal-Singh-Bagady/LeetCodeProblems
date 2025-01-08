class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                str1 = words[i]
                str2 = words[j]
                if str2.startswith(str1) and str2.endswith(str1):
                    count += 1
        return count
