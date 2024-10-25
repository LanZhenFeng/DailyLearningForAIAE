#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#


# @lc code=start
class Solution:

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 贪心
        '''
        82/82 cases passed (18 ms)
        Your runtime beats 96.24 % of python3 submissions
        Your memory usage beats 88.3 % of python3 submissions (16.4 MB)
        '''
        # for i in range(k):
        #     nums.sort()
        #     nums[0] = -nums[0]
        # return sum(nums)

        # 贪心，减少sort的使用
        '''
        82/82 cases passed (1 ms)
        Your runtime beats 98.6 % of python3 submissions
        Your memory usage beats 70.69 % of python3 submissions (16.5 MB)
        '''
        nums.sort(key=lambda x: abs(x), reverse=True)
        for i in range(len(nums)):
            if nums[i] < 0 and k:
                nums[i] *= -1
                k -= 1
        if k % 2 == 1: nums[-1] *= -1
        return sum(nums)


# @lc code=end
