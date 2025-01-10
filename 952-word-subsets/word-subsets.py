class Solution:
    def wordSubsets(self, words1, words2):
        count2 = dict()
        for word in words2:
            for letter in word:
                count2[letter] = max(count2.get(letter, 0), word.count(letter))

        ans = []
        for word in words1:
            universal = True
            for letter in count2:
                if word.count(letter) < count2[letter]:
                    universal = False
                    break
            if universal:
                ans.append(word)

        return ans
