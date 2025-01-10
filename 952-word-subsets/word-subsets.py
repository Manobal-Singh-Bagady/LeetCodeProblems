class Solution:
    def wordSubsets(self, words1, words2):
        count2 = dict()
        for word in words2:
            for letter in word:
                count2[letter] = max(count2.get(letter, 0), word.count(letter))

        ans = []
        for word in words1:
            if all(word.count(letter) >= count2.get(letter) for letter in count2):
                ans.append(word)

        return ans
