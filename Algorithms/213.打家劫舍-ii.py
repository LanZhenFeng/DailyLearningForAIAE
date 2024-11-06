#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#


# @lc code=start
class Solution:

    def rob(self, nums: List[int]) -> int:

        # DP
        # 时间复杂度: O(n)
        # 空间复杂度: O(n)
        '''
        75/75 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 17.51 % of python3 submissions (16.5 MB)
        '''
        # if len(nums) == 1: return nums[0]
        # dp1 = [0] * len(nums)
        # dp2 = [0] * len(nums)
        # dp1[0] = nums[0]
        # dp1[1] = max(nums[0], nums[1])
        # for i in range(2, len(nums) - 1):
        #     dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
        # dp2[0] = 0
        # dp2[1] = nums[1]
        # for i in range(2, len(nums)):
        #     dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
        # return max(dp1[-2], dp2[-1])

        # DP 2维
        # 时间复杂度: O(n)
        # 空间复杂度: O(n)
        '''
        75/75 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 24.38 % of python3 submissions (16.5 MB)
        '''

        def rob_action(nums: List[int]):
            dp = [[0, 0] for _ in range(len(nums))]
            dp[0][1] = nums[0]

            for i in range(1, len(nums)):
                dp[i][0] = max(dp[i - 1])
                dp[i][1] = dp[i - 1][0] + nums[i]

            return max(dp[-1])

        if len(nums) < 3: return max(nums)

        res1 = rob_action(nums[1:])
        res2 = rob_action(nums[:-1])

        return max(res1, res2)


# @lc code=end
