class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        ans = []
        def solve(start, end, sentence): 
            
            if end == len(s) + 1: 
                if ''.join(sentence) == s:
                    ans.append(' '.join(sentence))
                return 
            
            if s[start:end] in wordDict: 
                solve(end, end+1, sentence + [s[start:end]])
            solve(start, end+1, sentence)
        
        solve(0, 1, [])
        return ans
        

        

        
        