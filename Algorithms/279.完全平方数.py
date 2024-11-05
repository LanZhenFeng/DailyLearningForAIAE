#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#


# @lc code=start
class Solution:

    def numSquares(self, n: int) -> int:
        # DP 完全背包 版本一 先遍历背包，再遍历物品 求排列 > 求组合
        # 时间复杂度: O(n * √n)
        # 空间复杂度: O(n)
        '''
        589/589 cases passed (4855 ms)
        Your runtime beats 5.04 % of python3 submissions
        Your memory usage beats 59.18 % of python3 submissions (16.6 MB)
        '''
        # import sys
        # dp = [sys.maxsize] * (n + 1)
        # dp[0] = 0
        # for j in range(1, n + 1):
        #     for i in range(1, int(n**0.5) + 1):
        #         dp[j] = min(dp[j], dp[j - i * i] + 1)
        #     # print(dp)
        # return dp[n]

        # DP 完全背包 版本二 先遍历物品，再遍历背包 求组合 < 求排列
        # 时间复杂度: O(n * √n)
        # 空间复杂度: O(n)
        '''
        589/589 cases passed (2457 ms)
        Your runtime beats 64.73 % of python3 submissions
        Your memory usage beats 29.65 % of python3 submissions (16.9 MB)
        '''
        import sys
        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0
        for i in range(1, int(n**0.5) + 1):
            for j in range(i * i, n + 1):
                dp[j] = min(dp[j], dp[j - i * i] + 1)
            # print(dp)
        return dp[n]


# @lc code=end
