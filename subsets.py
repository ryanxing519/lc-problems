class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def solve(index, arr):
            if index == len(nums):
                ans.append(arr.copy())
                return

            arr.append(nums[index])
            solve(index+1, arr)
            arr.pop()
            solve(index+1, arr)

        solve(0, [])
        return ans
