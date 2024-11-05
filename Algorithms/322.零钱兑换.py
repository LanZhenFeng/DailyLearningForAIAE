#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#


# @lc code=start
class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP 完全背包
        '''
        189/189 cases passed (701 ms)
        Your runtime beats 93.88 % of python3 submissions
        Your memory usage beats 80.26 % of python3 submissions (16.7 MB)
        '''
        import sys
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j - coin] + 1, dp[j])
            # print(coins[i], dp)
        if dp[amount] == sys.maxsize: return -1
        return dp[amount]


# @lc code=end
