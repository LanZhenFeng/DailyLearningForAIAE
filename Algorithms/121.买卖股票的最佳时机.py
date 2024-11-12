#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#


# @lc code=start
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        # 暴力搜索 超时
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)
        '''
        Time Limit Exceeded
        # 198/212 cases passed (N/A)
        '''
        # maxv = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         maxv = max(maxv, prices[j] - prices[i])

        # return maxv

        # 贪心
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        '''
        212/212 cases passed (144 ms)
        Your runtime beats 39.47 % of python3 submissions
        Your memory usage beats 28.58 % of python3 submissions (25.6 MB)
        '''
        # maxv = 0
        # minv = prices[0]
        # for i in range(1, len(prices)):
        #     minv = min(minv, prices[i])
        #     maxv = max(maxv, prices[i] - minv)
        # return maxv

        # DP 版本1 O(n)空间
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # dp = [[0] * 2 for _ in range(len(prices))]
        # dp[0][0] = -prices[0]
        # dp[0][1] = 0

        # for i in range(1, len(prices)):
        #     dp[i][0] = max(dp[i - 1][0], -prices[i])
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        #     print(dp)
        # return max(dp[-1])

        # DP 版本2 O(1)空间
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        '''
        212/212 cases passed (178 ms)
        Your runtime beats 21.18 % of python3 submissions
        Your memory usage beats 80.99 % of python3 submissions (25.5 MB)
        '''
        dp = [0] * 2
        dp[0] = -prices[0]
        dp[1] = 0

        for i in range(1, len(prices)):
            dp[0] = max(dp[0], -prices[i])
            dp[1] = max(dp[1], dp[0] + prices[i])
        return dp[1]


# @lc code=end
