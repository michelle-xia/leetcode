class Solution:
    def combinationSum(self, candidates, target):
        out = []
        
        if len(candidates) == 0:
            return
        
        def dfs(candidates, target, path):
            if target == 0:
                out.append(path)
            for i in range(len(candidates)):
                if candidates[i] <= target:
                    dfs(candidates[i:], target - candidates[i], path + [candidates[i]])
    
        dfs(candidates, target, [])
        return out