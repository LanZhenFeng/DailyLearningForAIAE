#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#


# @lc code=start
class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        # 暴力搜索 Brute-Force Python超时
        '''
        Time Limit Exceeded
        202/210 cases passed (N/A)
        '''
        # if len(nums) == 1: return nums[0]
        # import sys
        # ans = -sys.maxsize
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         if sum > ans:
        #             ans = sum
        # return ans

        # 贪心
        '''
        210/210 cases passed (20 ms)
        Your runtime beats 99.88 % of python3 submissions
        Your memory usage beats 16.18 % of python3 submissions (30.9 MB)
        '''
        # import sys
        # ans = -sys.maxsize
        # count = 0
        # for i in range(len(nums)):
        #     count += nums[i]
        #     if count > ans:
        #         ans = count
        #     if count <= 0: count = 0
        # return ans

        # TODO 动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        '''
        210/210 cases passed (79 ms)
        Your runtime beats 63.27 % of python3 submissions
        Your memory usage beats 98.72 % of python3 submissions (30.2 MB
        '''
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


# @lc code=end
