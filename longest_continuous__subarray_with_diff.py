from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        # mins: 3
        # maxes: 2 3   

        # 2 4 2 0 2 2  
        ans = l = 0 
        mins = deque([])
        maxes = deque([])

        for r in range(len(nums)): 
            while mins and nums[r] < nums[mins[-1]]: mins.pop() 
            while maxes and nums[r] > nums[maxes[-1]]: maxes.pop() 
            mins.append(r)
            maxes.append(r) 

            # while the difference between these two is too large, keep popping
            while abs(nums[mins[0]] - nums[maxes[0]]) > limit: 
                if mins[0] < maxes[0]: temp = mins.popleft()
                else: temp = maxes.popleft() 
                l = temp + 1

            ans = max(ans, r - l + 1)

        return ans