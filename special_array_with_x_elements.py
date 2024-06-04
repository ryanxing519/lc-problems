class Solution:
    def specialArray(self, nums: List[int]) -> int:

        nums.sort(reverse=True)
        if nums[-1] >= len(nums): 
            return len(nums)
        for x in range(1, len(nums) + 1):
            if nums[x - 1] >= x and x < len(nums) and nums[x] < x:
                return x

        return -1