#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#


# @lc code=start
class Solution:

    def longestPalindromeSubseq(self, s: str) -> int:
        # DP
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        '''
        86/86 cases passed (729 ms)
        Your runtime beats 71.99 % of python3 submissions
        Your memory usage beats 91.64 % of python3 submissions (32.4 MB)
        '''
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]


# @lc code=end
