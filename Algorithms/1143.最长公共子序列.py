#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#


# @lc code=start
class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # DP 2维
        # 时间复杂度：O(n × m)，n 为A长度，m为B长度
        # 空间复杂度：O(n × m)
        '''
        47/47 cases passed (493 ms)
        Your runtime beats 53.95 % of python3 submissions
        Your memory usage beats 66.02 % of python3 submissions (41.1 MB)
        '''
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                # if dp[i][j] > res: res = dp[i][j]
            # print(i, j, dp)
        return dp[-1][-1]

        # TODO DP 1维


# @lc code=end
