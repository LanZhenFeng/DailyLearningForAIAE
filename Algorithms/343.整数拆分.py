#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#


# @lc code=start
class Solution:

    def integerBreak(self, n: int) -> int:
        # 动态规划
        # 时间复杂度 O(n^2)
        # 空间复杂度 O(n)
        '''
        50/50 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 79.27 % of python3 submissions (16.3 MB)
        '''
        # dp = [0] * (n + 1)
        # dp[2] = 1

        # for i in range(3, n + 1):
        #     for j in range(1, i // 2 + 1):
        #         dp[i] = max(dp[i], max((i - j) * j, dp[i - j] * j))

        # return dp[n]

        # 贪心 需要数学证明
        '''
        50/50 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 16.54 % of python3 submissions (16.5 MB)
        '''
        if n == 2: return 1
        if n == 3: return 2
        if n == 4: return 4
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        res *= n
        return res


# @lc code=end
