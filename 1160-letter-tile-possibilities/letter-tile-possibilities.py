class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seen = set()
        return self.genSeq("", 0, seen, "".join(sorted(tiles))) - 1

    def genSeq(self, curr: str, pos: int, seen: set, tiles: str) -> int:
        if pos >= len(tiles):
            if curr not in seen:
                seen.add(curr)
                return self.perms(curr)
            return 0
        return self.genSeq(curr, pos + 1, seen, tiles) + self.genSeq(
            curr + tiles[pos], pos + 1, seen, tiles
        )

    def perms(self, string: str) -> int:
        """
            n!
        ---------
        n1! * n2!

        where,
        n = total no of tiles
        n1 = freq of 1st tile
        n2 = freq of 2nd tile
        """
        total = factorial(len(string))
        for count in Counter(string).values():
            total //= factorial(count)
        return total
