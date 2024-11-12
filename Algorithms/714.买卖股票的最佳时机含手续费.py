#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#


# @lc code=start
class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        # DP 版本1
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        '''
        44/44 cases passed (223 ms)
        Your runtime beats 58.24 % of python3 submissions
        Your memory usage beats 61.6 % of python3 submissions (26.2 MB)
        '''
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)

        # print(dp)
        return dp[-1][-1]

        # TODO 优化空间复杂度

        # TODO 贪心


# @lc code=end
