class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = []
        for i in range(n):
            word = words[i]
            for j in range(n):
                if j!=i:
                    if word in words[j]:
                        ans.append(word)
                        break
        return ans
        