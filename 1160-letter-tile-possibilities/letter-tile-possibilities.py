class Solution:
    def genSeq(self, curr: str, seq: set, used: List[bool], tiles: str):
        seq.add(curr)
        for i in range(len(tiles)):
            if not used[i] and curr+tiles[i] not in seq:
                used[i] = True
                self.genSeq(curr + tiles[i], seq, used, tiles)
                used[i] = False

    def numTilePossibilities(self, tiles: str) -> int:
        seq = set()
        used = [False] * len(tiles)

        self.genSeq("", seq, used, tiles)

        return len(seq) - 1
