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
        profit = 0
        pre_prices = prices[:-1]
        suf_prices = prices[1:]
        for i in range(len(pre_prices)):
            if suf_prices[i] > pre_prices[i]:
                profit += suf_prices[i] - pre_prices[i]
        return profit

        # TODO 动态规划


# @lc code=end
