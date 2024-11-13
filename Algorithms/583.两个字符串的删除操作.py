#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#


# @lc code=start
class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        # DP 版本1
        '''
        1306/1306 cases passed (131 ms)
        Your runtime beats 68.12 % of python3 submissions
        Your memory usage beats 73.28 % of python3 submissions (18.5 MB)
        '''
        # dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        # for i in range(1, len(word1) + 1):
        #     for j in range(1, len(word2) + 1):
        #         if word1[i - 1] == word2[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1] + 1
        #         else:
        #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        #     # print(i, j, dp)

        # return len(word1) + len(word2) - 2 * dp[-1][-1]

        # DP 版本2
        '''
        1306/1306 cases passed (162 ms)
        Your runtime beats 31.61 % of python3 submissions
        Your memory usage beats 15.15 % of python3 submissions (20.3 MB)
        '''
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(1, len(word1) + 1):
            dp[i][0] = i

        for j in range(1, len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1,
                                   dp[i - 1][j - 1] + 2)
            # print(i, j, dp)

        return dp[-1][-1]


# @lc code=end
