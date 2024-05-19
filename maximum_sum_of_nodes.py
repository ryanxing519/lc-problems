class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        count = ans = 0 
        remove = float('inf')

        for num in nums: 
            sum = max(num, num ^ k)
            if sum > num: 
                count += 1
                remove = min(remove, sum - num)
            ans += sum 
            
        return ans if count % 2 == 0 else ans - remove
