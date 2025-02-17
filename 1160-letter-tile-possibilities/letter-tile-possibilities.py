class Solution:
    def genCount(self, freq: List[int]):
        total = 0
        for i in range(26):
            if freq[i] == 0:
                continue
            total += 1
            freq[i] -= 1
            total += self.genCount(freq)
            freq[i] += 1
        return total

    def numTilePossibilities(self, tiles: str) -> int:
        count = [0]*26
        for i in tiles:
            count[ord(i)-65]+=1
        return self.genCount(count)
