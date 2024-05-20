class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def solve(index, sum): 
            if index == len(nums): 
                return sum
            
            return solve(index+1, sum^nums[index]) + solve(index+1, sum)
            
        return solve(0, 0)