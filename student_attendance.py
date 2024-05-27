class Solution:
    def checkRecord(self, n: int) -> int:
        
        cache = [[[-1]*3 for _ in range(2)] for _ in range(n)]
        def solve(index, absent, late): 
            # we can't have 3 L's in a row
            # we can't have a total of 2 absences
            if index == n: 
                return 1
            
            if cache[index][absent][late] != -1: 
                return cache[index][absent][late]
            
            ans = 0
            if absent == 0: 
                ans = (ans+solve(index+1, 1, 0)) % (10**9 + 7)
            if late < 2: 
                ans = (ans+solve(index+1, absent, late + 1)) % (10**9 + 7)
            ans = (ans+solve(index+1, absent, 0)) % (10**9 + 7)
            cache[index][absent][late] = ans
            return ans

        return solve(0, 0, 0)