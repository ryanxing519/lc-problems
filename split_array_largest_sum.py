class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        #binary search the answer, try to get as close as possible

        def check(max_sum):
            sum, split = 0, 1
            for num in nums:
                if sum + num > max_sum:
                    split += 1
                    sum = 0
                sum += num
            return split <= k

        l, r = max(nums), sum(nums)

        while l < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l


