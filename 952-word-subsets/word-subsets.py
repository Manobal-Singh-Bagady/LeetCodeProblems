from collections import Counter


class Solution:
    def wordSubsets(self, words1, words2):
        letter_count = dict()
        for word in words2:
            count = Counter(word)
            for letter in count:
                letter_count[letter] = max(letter_count.get(letter, 0), count[letter])

        ans = []
        for word in words1:
            count = Counter(word)
            if all(count.get(letter, 0) >= letter_count.get(letter) for letter in letter_count):
                ans.append(word)

        return ans
