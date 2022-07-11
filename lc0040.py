class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        self.dfs(candidates, [], 0, target, res)
        return res

    def dfs(self, candidates, path, start, target, res):
        if target == 0:
            res.append(path)
            return

        visited = set()
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            if candidates[i] not in visited:
                visited.add(candidates[i])
                self.dfs(candidates, path + [candidates[i]], i + 1, target - candidates[i], res)