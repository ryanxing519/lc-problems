import collections

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        #so we'll recursively generate subsets, and keep track of a set
        # two sum idea, we'll keep track of a set that has all the elements in it

        # 2 4 6

        def solve(index, dict):
            if index == len(nums): 
                return 1 

            ans = 0 
            if not (dict[nums[index] + k] or dict[nums[index] - k]): 
                dict[nums[index]] += 1
                ans += solve(index+1, dict)

            if dict[nums[index]]: 
                dict[nums[index]] -= 1
            ans += solve(index+1, set)

            return ans 

        
        return solve(0, collections.defaultdict(int)) - 1
    
    # if its already in there, and we remove it, why is this an issue

    # 1 1 1 2
    # 