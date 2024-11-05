#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#


# @lc code=start
class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        # DP 完全背包
        '''
        29/29 cases passed (111 ms)
        Your runtime beats 83.64 % of python3 submissions
        Your memory usage beats 84.8 % of python3 submissions (16.5 MB)
        '''
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        # print(dp)
        return dp[amount]


# @lc code=end
