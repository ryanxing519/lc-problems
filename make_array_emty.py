class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        # first pass takes n operations, initiate ans to n

        # if everything is in order, then great we did our job, 1 2 3 4 5
        # n = 5 were done

        # the second we hit an out of order sort of index, then we need more moves
        # we have to add at least the remaining number of indexes for operations
        # if those remaining indexes were in order, great, then we dont need to add any more
        # we always make the number of remaining elements moves to return to the original order

        # eg: 1 2 4 3 5
        # remove 1 2 3 in 3 moves, use another 2 to push 4 and 5 back to their order
        # 4 5
        # now 4 was out of order, so we need at least 2 more moves
        # add 2
        # 5 was after 4 so we dont need to add any more

        # 1 5 2 3 6 4
        # remove 1 2 3, and then restore the order of the original array, this takes 6 (n) moves
        # 5 6 4
        # reomve 4 this pass and since 5 is before 4, we need to add at least 2 more moves again
        # 6 is after 5, so we handled this already
        ans = n = len(nums)

        nums = [(nums[i], i) for i in range(len(nums))]
        nums.sort()

        for i in range(1, n):
            if nums[i][1] < nums[i - 1][1]:
                ans += n - i

        return ans
