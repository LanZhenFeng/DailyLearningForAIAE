#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#


# @lc code=start
class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 动态规划 版本一
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        '''
        284/284 cases passed (3 ms)
        Your runtime beats 81.65 % of python3 submissions
        Your memory usage beats 18.25 % of python3 submissions (16.7 MB)
        '''
        # dp = [0] * (len(cost) + 1)
        # for i in range(2, len(cost) + 1):
        #     dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        # return dp[-1]

        # 动态规划 版本一
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        '''
        284/284 cases passed (3 ms)
        Your runtime beats 81.65 % of python3 submissions
        Your memory usage beats 84.29 % of python3 submissions (16.4 MB)
        '''
        dp_l, dp_r = 0, 0
        for i in range(2, len(cost) + 1):
            dp_l, dp_r = dp_r, min(dp_l + cost[i - 2], dp_r + cost[i - 1])
        return dp_r


# @lc code=end
