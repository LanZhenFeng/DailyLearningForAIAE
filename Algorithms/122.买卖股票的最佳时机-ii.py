#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#


# @lc code=start
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        # 贪心
        '''
        200/200 cases passed (2 ms)
        Your runtime beats 98.1 % of python3 submissions
        Your memory usage beats 36.04 % of python3 submissions (17.6 MB)
        '''
        # profit = 0
        # buy_price = -1
        # sell_price = -1
        # i = 0
        # while i <= len(prices) - 1:
        #     buy_price = prices[i]
        #     j = i
        #     while j + 1 < len(prices) and prices[j + 1] > prices[j]:
        #         j += 1
        #     sell_price = prices[j]
        #     profit += sell_price - buy_price
        #     i = j + 1

        # return profit

        # 贪心 只收集正利润
        '''
        200/200 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 31.18 % of python3 submissions (18 MB)
        '''
        # profit = 0
        # pre_prices = prices[:-1]
        # suf_prices = prices[1:]
        # for i in range(len(pre_prices)):
        #     if suf_prices[i] > pre_prices[i]:
        #         profit += suf_prices[i] - pre_prices[i]
        # return profit

        # TODO DONE 动态规划  O(n)空间
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        '''
        200/200 cases passed (3 ms)
        Your runtime beats 65.7 % of python3 submissions
        Your memory usage beats 32.39 % of python3 submissions (17.7 MB)
        '''
        # dp = [[0] * 2] * len(prices)
        # dp[0][0] = -prices[0]
        # dp[0][1] = 0

        # for i in range(1, len(prices)):
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        # return dp[-1][-1]

        # 动态规划 O(1)空间
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        '''
        200/200 cases passed (3 ms)
        Your runtime beats 65.53 % of python3 submissions
        Your memory usage beats 63.48 % of python3 submissions (17.5 MB)
        '''
        dp = [0] * 2
        dp[0] = -prices[0]
        dp[1] = 0

        for i in range(1, len(prices)):
            dp[0] = max(dp[0], dp[1] - prices[i])
            dp[1] = max(dp[1], dp[0] + prices[i])
        return dp[1]


# @lc code=end
