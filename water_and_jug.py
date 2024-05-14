class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        
        seen = set([])
        def solve(total): 

            if total == target: 
                return True
            if total in seen or not (0 <= total <= x + y): 
                return False
            
            seen.add(total)

            return solve(total + x) or solve(total - x) or solve(total + y) or solve(total - y)
        
        return solve(0)
