from collections import Counter


class Solution:
    def wordSubsets(self, words1, words2):
        letter_count = dict()
        for word in words2:
            for letter in word:
                letter_count[letter] = max(letter_count.get(letter, 0), word.count(letter))

        ans = []
        for word in words1:
            if all(word.count(letter) >= letter_count.get(letter) for letter in letter_count):
                ans.append(word)

        return ans
