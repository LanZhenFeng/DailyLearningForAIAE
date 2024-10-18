#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#


# @lc code=start
class Solution:

    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        # 回溯
        '''
        160/160 cases passed (11 ms)
        Your runtime beats 99.79 % of python3 submissions
        Your memory usage beats 9.32 % of python3 submissions (16.7 MB)
        '''

        # def backtracking(candidates, target, start, path, ans) -> None:
        #     if sum(path) == target:
        #         ans.append(path[:])
        #         return None
        #     if sum(path) > target:
        #         return None
        #     # for candidate in candidates:
        #     for i in range(start, len(candidates)):
        #         path.append(candidates[i])
        #         backtracking(candidates, target, i, path, ans)
        #         path.pop()

        # ans = []
        # backtracking(candidates, target, 0, [], ans)

        # return ans


        # 回溯 + 剪枝
        '''
        160/160 cases passed (3 ms)
        Your runtime beats 99.97 % of python3 submissions
        Your memory usage beats 14.92 % of python3 submissions (16.6 MB)
        '''

        def backtracking(candidates, target, start, path, ans) -> None:
            if sum(path) == target:
                ans.append(path[:])
                return None
            if sum(path) > target:
                return None
            # for candidate in candidates:
            for i in range(start, len(candidates)):
                if sum(path) + candidates[i] > target:
                    break
                path.append(candidates[i])
                backtracking(candidates, target, i, path, ans)
                path.pop()

        ans = []
        candidates.sort()
        backtracking(candidates, target, 0, [], ans)

        return ans



# @lc code=end
