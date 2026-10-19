class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        j = len(people)-1
        i = 0
        count = 0

        people.sort()
        while i <= j:

            if people[i] + people[j] <=limit:

                i +=1

            j -=1

            count +=1


        return count