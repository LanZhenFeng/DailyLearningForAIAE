#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#


# @lc code=start
class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP
        # 时间复杂度: O(n^2)
        # 空间复杂度: O(n)
        if len(nums) == 1: return 1
        dp = [1] * len(nums)
        res = 0

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                if dp[i] > res:
                    res = dp[i]
        return res

        # TODO 贪心


# @lc code=end
