from collections import Counter
from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # [1,2,3,6,2,3,4,7,8]

        # 1: 1
        # idea is to loop through the counts sorted:
        # for each count, we need to iterate the group size, and then decrease each numbers remaining count by the current numbers count
        # if we ever get a negative count, that means we couldn't make the straight

        #eg 1 1 2 3, if we have 2 ones and k is 3 here, then we would need 2 2's and 2 3's, but we don't have those and we should return false

        cnts = Counter(hand)

        for key in sorted(cnts.keys()):
            amt = cnts[key]
            for i in range(groupSize):
                cnts[key+i] -= amt
                if cnts[key+i] < 0: return False

        return True

tester = Solution()
tester.isNStraightHand([1,2,3,6,2,3,4,7,8], 4)
