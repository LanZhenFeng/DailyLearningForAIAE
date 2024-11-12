#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#


# @lc code=start
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        # DP 版本1
        # 时间复杂度 O(n)
        # 空间复杂度 O(n*5)
        '''
        214/214 cases passed (520 ms)
        Your runtime beats 55.74 % of python3 submissions
        Your memory usage beats 29.01 % of python3 submissions (42 MB)
        '''

        # dp = [[0] * 5 for _ in range(len(prices))]
        # dp[0][1] = -prices[0]
        # dp[0][3] = -prices[0]

        # for i in range(1, len(prices)):
        #     dp[i][1] = max(dp[i - 1][1], -prices[i])
        #     dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
        #     dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
        #     dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
        # # print(dp)
        # return dp[-1][-1]

        # DP 版本2
        # 时间复杂度 O(n)
        # 空间复杂度 O(n*5)
        '''
        214/214 cases passed (529 ms)
        Your runtime beats 53.22 % of python3 submissions
        Your memory usage beats 27.11 % of python3 submissions (42.1 MB)
        '''

        # dp = [[0] * 5 for _ in range(len(prices))]
        # dp[0][1] = -prices[0]
        # dp[0][3] = -prices[0]

        # for i in range(1, len(prices)):
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        #     dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
        #     dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
        #     dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
        # # print(dp)
        # return dp[-1][-1]

        # DP 版本3
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        '''
        214/214 cases passed (298 ms)
        Your runtime beats 77.55 % of python3 submissions
        Your memory usage beats 76.04 % of python3 submissions (27.7 MB)
        '''

        dp = [0] * 5
        dp[1] = -prices[0]
        dp[3] = -prices[0]

        for i in range(1, len(prices)):
            dp[1] = max(dp[1], dp[0] - prices[i])
            dp[2] = max(dp[2], dp[1] + prices[i])
            dp[3] = max(dp[3], dp[2] - prices[i])
            dp[4] = max(dp[4], dp[3] + prices[i])
        # print(dp)
        return dp[-1]


# @lc code=end
