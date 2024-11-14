#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#


# @lc code=start
class Solution:

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 单调栈
        '''
        223/223 cases passed (55 ms)
        Your runtime beats 12.13 % of python3 submissions
        Your memory usage beats 25.11 % of python3 submissions (18.3 MB)
        '''
        res = [-1] * len(nums)
        stack = []
        for i in range(len(nums) * 2):
            while stack and nums[i % len(nums)] > nums[stack[-1]]:
                res[stack[-1]] = nums[i % len(nums)]
                stack.pop()
            stack.append(i % len(nums))

        return res


# @lc code=end
