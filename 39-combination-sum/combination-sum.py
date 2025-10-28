class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        arr =[]
        self.dfs(candidates, target, [], arr)
        return arr

    def dfs(self, candidates, target, path, arr):
        if target <0:
            return
        if target == 0:
            arr.append(path)
            return
        for i in range(len(candidates)):
            self.dfs(candidates[i:], target-candidates[i],path+[candidates[i]], arr)
        