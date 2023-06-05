class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        s_people = sorted(people)
        count = 0
        l = 0
        r = len(s_people) - 1
        while l <= r:
            if s_people[l] + s_people[r] <= limit:
                l+=1
            r-=1
            count+=1
        return count
         