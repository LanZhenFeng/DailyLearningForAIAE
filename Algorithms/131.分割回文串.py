#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#


# @lc code=start
class Solution:

    def partition(self, s: str) -> List[List[str]]:
        # 回溯 + 剪枝
        '''
        32/32 cases passed (51 ms)
        Your runtime beats 99.83 % of python3 submissions
        Your memory usage beats 86.42 % of python3 submissions (31 MB)
        '''

        def backtracking(s, start, path, ans) -> None:
            if start == len(s):
                # print(path)
                ans.append(path[:])
                return None

            for i in range(start, len(s)):
                # print(s[start:i+1])
                if s[start:i + 1] != s[start:i + 1][::-1]: continue
                path.append(s[start:i + 1])
                backtracking(s, i + 1, path, ans)
                path.pop()

        ans = []
        backtracking(s, 0, [], ans)

        return ans


# @lc code=end
