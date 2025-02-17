class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seen = set()

        tiles = "".join(sorted(tiles))

        return self.genSeq(tiles, "", 0, seen) - 1

    def genSeq(self, tiles: str, curr: str, pos: int, seen: Set[str]) -> int:
        if pos >= len(tiles):
            if curr not in seen:
                seen.add(curr)
                return self.perms(curr)
            return 0
        return self.genSeq(tiles, curr, pos + 1, seen) + self.genSeq(
            tiles, curr + tiles[pos], pos + 1, seen
        )

    def perms(self, string: str) -> int:
        total = factorial(len(string))
        for count in Counter(string).values():
            total //= factorial(count)
        return total
