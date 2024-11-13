#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#


# @lc code=start
class Solution:

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # DP
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        '''
        35/35 cases passed (3 ms)
        Your runtime beats 71.25 % of python3 submissions
        Your memory usage beats 20.93 % of python3 submissions (17.5 MB)
        '''
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        # print(dp)
        return max(dp)

        # TODO 贪心


# @lc code=end
