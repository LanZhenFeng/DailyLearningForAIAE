#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#


# @lc code=start
class Solution:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 回溯
        '''
        18/18 cases passed (1 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 50.14 % of python3 submissions (16.4 MB)
        '''
        # def backtracking(k, n, start, path, ans):
        #     if len(path) == k and sum(path) == n:
        #         ans.append(path[:])
        #         return

        #     for i in range(start, 10):
        #         path.append(i)
        #         backtracking(k, n, i + 1, path, ans)
        #         path.pop()

        # ans = []
        # backtracking(k, n, 1, [], ans)

        # return ans

        # 回溯 + 剪枝
        '''
        18/18 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 76.73 % of python3 submissions (16.3 MB)
        '''

        def backtracking(k, n, start, path, ans):
            if (sum(path) > n): return
            if len(path) == k:
                if sum(path) == n:
                    ans.append(path[:])
                return
            for i in range(start, 10 - (k - len(path)) + 1):
                path.append(i)
                backtracking(k, n, i + 1, path, ans)
                path.pop()

        ans = []
        backtracking(k, n, 1, [], ans)

        return ans


# @lc code=end
