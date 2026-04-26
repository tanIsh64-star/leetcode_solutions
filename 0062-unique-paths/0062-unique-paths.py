class Solution:
    def uniquePaths(self, m, n):
        N = m + n - 2
        r = min(m - 1, n - 1)
        
        result = 1
        for i in range(r):
            result = result * (N - i) // (i + 1)
        
        return result