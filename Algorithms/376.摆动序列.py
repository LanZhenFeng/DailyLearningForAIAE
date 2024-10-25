#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#


# @lc code=start
class Solution:

    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 贪心 严格的峰或谷才能+1，即单调性转变时
        '''
        32/32 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 71.71 % of python3 submissions (16.4 MB)
        '''
        ans = 1
        trend = 0

        for i in range(1, len(nums)):
            if (trend <= 0
                    and nums[i] > nums[i - 1]) or (trend >= 0
                                                   and nums[i] < nums[i - 1]):
                ans += 1
            if nums[i] > nums[i - 1]:
                trend = 1
            elif nums[i] < nums[i - 1]:
                trend = -1

        return ans

        # TODO 动规


# @lc code=end
