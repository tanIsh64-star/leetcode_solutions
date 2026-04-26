class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        
        def backtrack(start, path, target):
            # Base case
            if target == 0:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Stop early if number exceeds target
                if candidates[i] > target:
                    break
                
                # Choose element
                path.append(candidates[i])
                
                # Move to next index (i+1 → no reuse)
                backtrack(i + 1, path, target - candidates[i])
                
                # Backtrack
                path.pop()
        
        backtrack(0, [], target)
        return result