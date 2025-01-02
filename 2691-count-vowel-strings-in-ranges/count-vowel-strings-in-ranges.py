class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vovels = {"a", "e", "i", "o", "u"}
        hash = dict()
        count = 0
        for i in range(len(words)):
            if words[i][0] in vovels and words[i][-1] in vovels:
                count += 1
            hash[i] = count

        ans = []
        for i in queries:
            ans.append(hash.get(i[1]) - hash.get(i[0] - 1, 0))
        return ans
