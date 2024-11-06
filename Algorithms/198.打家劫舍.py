#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#


# @lc code=start
class Solution:

    def rob(self, nums: List[int]) -> int:
        # DP 版本一
        # 时间复杂度: O(n)
        # 空间复杂度: O(n)
        '''
        70/70 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 11.32 % of python3 submissions (16.6 MB)
        '''
        # dp = [0] * (len(nums) + 1)
        # dp[1] = nums[0]
        # for i in range(2, len(nums) + 1):
        #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        # # print(dp)
        # return dp[-1]

        # DP 版本二
        # 时间复杂度: O(n)
        # 空间复杂度: O(n)
        '''
        70/70 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 6.12 % of python3 submissions (16.6 MB)
        '''
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        # print(dp)
        return dp[-1]


# @lc code=end
