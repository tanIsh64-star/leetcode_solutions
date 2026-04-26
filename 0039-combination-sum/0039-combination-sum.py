class Solution:
    def combinationSum(self, candidates, target):
        result = []
        
        def backtrack(start, path, target):
            # Base case
            if target == 0:
                result.append(path[:])
                return
            
            if target < 0:
                return
            
            # Try all candidates from current index
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                
                # Stay at i (reuse same element)
                backtrack(i, path, target - candidates[i])
                
                # Backtrack
                path.pop()
        
        backtrack(0, [], target)
        return result