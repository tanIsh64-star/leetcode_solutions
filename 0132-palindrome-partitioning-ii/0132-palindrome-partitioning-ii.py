class Solution:
    def minCut(self, s):
        n = len(s)
        
        dp = [i - 1 for i in range(n + 1)]
        
        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                dp[r + 1] = min(dp[r + 1], dp[l] + 1)
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                dp[r + 1] = min(dp[r + 1], dp[l] + 1)
                l -= 1
                r += 1
        
        return dp[n]