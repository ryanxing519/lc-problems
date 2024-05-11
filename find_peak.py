class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # binary search, take the mid, check the left and right of it to see if its a peak, if it is return
        # if the mid is bigger than the left, then we are guarenteed a peak on the right
        # if the mid is smaller than the left, we are guarenteed a peak on the left

        if len(nums) == 1 or nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return len(nums)-1

        l, r = 1, len(nums)-2

        while l <= r:
            m = (l + r) // 2

            if nums[m-1] < nums[m] > nums[m+1]:
                return m
            elif nums[m] > nums[m-1]:
                l = m + 1
            else:
                r = m - 1
    