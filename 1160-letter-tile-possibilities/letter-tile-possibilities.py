class Solution:
    def genCount(self, freq: Dict[str, int]):
        total = 0
        for i in freq:
            if freq[i] == 0:
                continue
            total += 1
            freq[i] -= 1
            total += self.genCount(freq)
            freq[i] += 1
        return total

    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        return self.genCount(count)
