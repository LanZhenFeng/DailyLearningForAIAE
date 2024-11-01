#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#


# @lc code=start
class Solution:

    def numTrees(self, n: int) -> int:
        # 动态规划 版本一
        # 时间复杂度 O(n^2)
        # 空间复杂度 O(n)
        '''
        19/19 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 65.85 % of python3 submissions (16.4 MB)
        '''
        # if n < 2: return 1
        # dp = [0] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n + 1):
        #     for j in range(1, i + 1):
        #         dp[i] += dp[j - 1] * dp[i - j]
        # return dp[n]

        # 动态规划 版本二
        # 时间复杂度 O(n^2)
        # 空间复杂度 O(n)
        '''
        19/19 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 79.87 % of python3 submissions (16.3 MB)
        '''
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


# @lc code=end
