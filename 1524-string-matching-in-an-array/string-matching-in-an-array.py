# fastest solution
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        all_words = ' '.join(words)
        return [word for word in words if all_words.count(word)>1]
        