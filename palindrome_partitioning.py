class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(string): 
            for i in range(len(string) // 2): 
                if string[i] != string[len(string) - i - 1]: 
                    return False
            return True
        
        ans = []
        def solve(start, end, partition): 
            if end == len(s):  
                if ''.join(partition) == s: ans.append(partition.copy())
                return 
            
            if is_palindrome(s[start:end]): 
                solve(end, end+1, partition + [s[start:end]])
            solve(start, end+1, partition)
            
        solve(0, 1, [])
        return ans
        
