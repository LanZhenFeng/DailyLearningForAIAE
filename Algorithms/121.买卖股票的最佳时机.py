#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#


# @lc code=start
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        # # 暴力搜索 超时
        # # 时间复杂度：O(n^2)
        # # 空间复杂度：O(1)
        # '''
        # Time Limit Exceeded
        # # 198/212 cases passed (N/A)
        # '''
        # # maxv = 0
        # # for i in range(len(prices)):
        # #     for j in range(i + 1, len(prices)):
        # #         maxv = max(maxv, prices[j] - prices[i])

        # # return maxv

        # # 贪心
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(1)
        # '''
        # 212/212 cases passed (144 ms)
        # Your runtime beats 39.47 % of python3 submissions
        # Your memory usage beats 28.58 % of python3 submissions (25.6 MB)
        # '''
        # # maxv = 0
        # # minv = prices[0]
        # # for i in range(1, len(prices)):
        # #     minv = min(minv, prices[i])
        # #     maxv = max(maxv, prices[i] - minv)
        # # return maxv

        # # DP 版本1 O(n)空间
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(n)
        # # dp = [[0] * 2 for _ in range(len(prices))]
        # # dp[0][0] = -prices[0]
        # # dp[0][1] = 0

        # # for i in range(1, len(prices)):
        # #     dp[i][0] = max(dp[i - 1][0], -prices[i])
        # #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        # #     print(dp)
        # # return max(dp[-1])

        # # DP 版本2 O(1)空间
        # # 时间复杂度 O(n)
        # # 空间复杂度 O(1)
        # '''
        # 212/212 cases passed (178 ms)
        # Your runtime beats 21.18 % of python3 submissions
        # Your memory usage beats 80.99 % of python3 submissions (25.5 MB)
        # '''
        # dp = [0] * 2
        # dp[0] = -prices[0]
        # dp[1] = 0

        # for i in range(1, len(prices)):
        #     dp[0] = max(dp[0], -prices[i])
        #     dp[1] = max(dp[1], dp[0] + prices[i])
        # return dp[1]

        # 暴力求解 超出时间限制
        # 时间复杂度 O(n^2)
        # 空间复杂度 O(1)
        # max_profit = 0
        # for i in range(len(prices)-1):
        #     cur_max = max(prices[i:]) - prices[i]
        #     max_profit = max(cur_max, max_profit)
        # return max_profit

        # 记录最小值
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        # max_profit = 0
        # cur_min = prices[0]
        # for i in range(1, len(prices)):
        #     max_profit = max(max_profit, prices[i] - cur_min)
        #     cur_min = min(prices[i], cur_min)
        # return max_profit

        # 记录最大值
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        # max_profit = 0
        # cur_max = prices[-1]
        # for i in range(len(prices)-2, -1, -1):
        #     max_profit = max(max_profit, cur_max - prices[i])
        #     cur_max = max(prices[i], cur_max)
        # return max_profit

        # 滑动窗口
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        # left, right, max_profit = 0, 0, 0
        # while right < len(prices):
        #     if left == right:
        #         right += 1
        #     elif prices[left] > prices[right]:
        #         left += 1
        #     else:
        #         max_profit = max(max_profit, prices[right] - prices[left])
        #         right += 1
        # return max_profit


        # DP
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        # dp = [[0] * 2 for _ in range(len(prices))]
        # dp[0][0] = -prices[0]
        # dp[0][1] = 0

        # for i in range(1, len(prices)):
        #     dp[i][0] = max(dp[i-1][0], -prices[i])
        #     dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        # return dp[-1][-1]

        # DP 优化
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        # dp = [[0] * 2 for _ in range(2)]
        # dp[0][0] = -prices[0]
        # dp[0][1] = 0

        # for i in range(1, len(prices)):
        #     dp[i%2][0] = max(dp[(i-1)%2][0], -prices[i])
        #     dp[i%2][1] = max(dp[(i-1)%2][1], dp[(i-1)%2][0] + prices[i])
        # return max(dp[1][-1], dp[0][-1])


# @lc code=end
