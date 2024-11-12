#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 买卖股票的最佳时机含冷冻期
#


# @lc code=start
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        # DP 版本1
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        '''
        210/210 cases passed (3 ms)
        Your runtime beats 72.88 % of python3 submissions
        Your memory usage beats 43.53 % of python3 submissions (17.2 MB)
        '''
        # dp = [[0] * 4 for _ in range(len(prices))]

        # dp[0][0] = -prices[0]
        # dp[0][1] = 0
        # dp[0][2] = 0
        # dp[0][3] = 0

        # for i in range(1, len(prices)):
        #     dp[i][0] = max(
        #         dp[i - 1][0],
        #         max(dp[i - 1][3] - prices[i], dp[i - 1][1] - prices[i]))
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
        #     dp[i][2] = dp[i - 1][0] + prices[i]
        #     dp[i][3] = dp[i - 1][2]
        # # print(dp)

        # return max(dp[-1][3], max(dp[-1][1], dp[-1][2]))

        # DP 版本1
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        '''
        210/210 cases passed (3 ms)
        Your runtime beats 72.88 % of python3 submissions
        Your memory usage beats 90.77 % of python3 submissions (16.7 MB)
        '''
        dp = [[0] * 4 for _ in range(2)]

        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0
        dp[0][3] = 0

        for i in range(1, len(prices)):
            dp[i % 2][0] = max(
                dp[(i - 1) % 2][0],
                max(dp[(i - 1) % 2][3] - prices[i],
                    dp[(i - 1) % 2][1] - prices[i]))
            dp[i % 2][1] = max(dp[(i - 1) % 2][1], dp[(i - 1) % 2][3])
            dp[i % 2][2] = dp[(i - 1) % 2][0] + prices[i]
            dp[i % 2][3] = dp[(i - 1) % 2][2]
        # print(dp)

        return max(
            dp[(len(prices) - 1) % 2][3],
            max(dp[(len(prices) - 1) % 2][1], dp[(len(prices) - 1) % 2][2]))


# @lc code=end
