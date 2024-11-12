#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#


# @lc code=start
class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        # DP 版本1
        # 时间复杂度 O(n)
        # 空间复杂度 O(n*2k)
        '''
        210/210 cases passed (67 ms)
        Your runtime beats 78.06 % of python3 submissions
        Your memory usage beats 51.19 % of python3 submissions (19.1 MB)
        '''
        # dp = [[0] * (2 * k + 1) for _ in range(len(prices))]
        # for i in range(1, 2 * k + 1, 2):
        #     dp[0][i] = -prices[0]

        # for i in range(1, len(prices)):
        #     for j in range(1, 2 * k + 1, 2):
        #         dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
        #         dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] + prices[i])
        # # print(dp)
        # return dp[-1][-1]

        # DP 版本2
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        '''
        210/210 cases passed (51 ms)
        Your runtime beats 93.08 % of python3 submissions
        Your memory usage beats 81.07 % of python3 submissions (16.6 MB)
        '''

        dp = [0] * (2 * k + 1)
        for i in range(1, 2 * k + 1, 2):
            dp[i] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(1, 2 * k + 1, 2):
                dp[j] = max(dp[j], dp[j - 1] - prices[i])
                dp[j + 1] = max(dp[j + 1], dp[j] + prices[i])
        # print(dp)
        return dp[-1]


# @lc code=end
