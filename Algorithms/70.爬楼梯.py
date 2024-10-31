#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#


# @lc code=start
class Solution:

    def climbStairs(self, n: int) -> int:
        # 动态规划 版本一
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        '''
        45/45 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 82.98 % of python3 submissions (16.3 MB)
        '''
        # dp = [1, 2]
        # for i in range(2, n):
        #     dp.append(dp[-1] + dp[-2])
        # return dp[n - 1]

        # 动态规划 版本二
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        '''
        45/45 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 58.96 % of python3 submissions (16.4 MB)
        '''
        if n == 1: return 1
        dp_l, dp_r = 1, 2
        for i in range(2, n):
            dp_l, dp_r = dp_r, dp_l + dp_r
        return dp_r


# @lc code=end
