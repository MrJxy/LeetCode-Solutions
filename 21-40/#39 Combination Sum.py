## #39 Combination Sum
## Date: 2017.02.26

class Solution(object):
    res = []

    def combinationSum(self, candidates, target):
        self.res = []
        self.recur(candidates, target, [])
        new_res = []
        for i in self.res:
            if i not in new_res:
                new_res.append(i)
        return new_res


    def recur(self, candidates, target, prev):
        if candidates == []: return []
        candidates.sort()
        if target < candidates[0]: return
        for i in candidates:
            if i < target:
                self.recur(candidates, target - i, sorted(prev + [i]))
            elif i == target:
                self.res.append(sorted(prev+[i]))
                return
            else:
                return

print(Solution().combinationSum([2], 1))