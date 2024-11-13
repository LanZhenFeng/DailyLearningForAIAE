#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#


# @lc code=start
class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        # DP
        # 时间复杂度: O(n * m)
        # 空间复杂度: O(n * m)
        '''
        66/66 cases passed (419 ms)
        Your runtime beats 60.98 % of python3 submissions
        Your memory usage beats 35.52 % of python3 submissions (71.7 MB)
        '''
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for i in range(len(s)):
            dp[i][0] = 1

        for j in range(1, len(t)):
            dp[0][j] = 0

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        # print(dp)
        return dp[-1][-1]


# @lc code=end
