#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#


# @lc code=start
class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        # 回溯法
        '''
        27/27 cases passed (135 ms)
        Your runtime beats 97.16 % of python3 submissions
        Your memory usage beats 32.13 % of python3 submissions (57.6 MB)
        '''

        # def backtracking(arr, ans, start_index, k):
        #     if k == 0:
        #         ans.append(arr.copy())
        #         return

        #     for i in range(start_index, n + 1):
        #         arr.append(i)
        #         backtracking(arr, ans, i + 1, k - 1)
        #         arr.pop()

        # arr = []
        # ans = []

        # backtracking(arr, ans, 1, k)
        # return ans

        # 回溯法
        '''
        27/27 cases passed (95 ms)
        Your runtime beats 98.38 % of python3 submissions
        Your memory usage beats 51.19 % of python3 submissions (57.5 MB)
        '''

        def backtracking(start_index, n, k):
            if len(arr) == k:
                ans.append(arr.copy())
                return

            for i in range(start_index, n + 1 - (k - len(arr)) + 1):
                arr.append(i)
                backtracking(i + 1, n, k)
                arr.pop()

        arr = []
        ans = []
        backtracking(1, n, k)
        return ans


# @lc code=end
