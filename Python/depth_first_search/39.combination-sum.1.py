class Solution:
    """
    @param: candidates: A list of integers
    @param: target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates.sort()
        if not candidates:
            return [[]]
        combination, start_index, result = [], 0, []
        self.dfs(combination, candidates, start_index, target, result)
        return result
    
    
    def dfs(self, combination, candidates, start_index, target, result):
        
        # [2,2,3,3,6,7] 5
        # [2(0), 3(2)]
        # ! [2(1), 3(1)]
        # ! [2(1), 3(2)]
        
        for i in range(start_index, len(candidates)):
            if (i != start_index and candidates[i] == candidates[i-1]):
                continue
            if candidates[i] > target:
                break
            if candidates[i] == target:
                result.append(combination[:] + [candidates[i]])
                break
            
            combination.append(candidates[i])
            self.dfs(
                combination, candidates, i,
                target-candidates[i], result)
            combination.pop()
        