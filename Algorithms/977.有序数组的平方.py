#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
from typing import List
# @lc code=start
class Solution:

    # def InsertSort(nums):
    #     for i in range(1, len(nums)):
    #         key = nums[i]
    #         j = i - 1
    #         while j >= 0 and nums[j] > key:
    #             nums[j+1] = nums[j]
    #             j -= 1
    #         nums[j+1] = key


    def QuickSort(nums, left, right):
        # if right - left < 5:
        #     Solution.InsertSort(nums)
        #     return
        left_bak = left
        right_bak = right
        baseline = nums[left]
        while left < right:
            while left < right and nums[right] >= baseline:
                right = right - 1
            nums[left] = nums[right]
            while left < right and nums[left] <= baseline:
                left = left + 1
            nums[right] = nums[left]
        nums[left] = baseline
        if left_bak < right - 1:
            Solution.QuickSort(nums, left_bak, right - 1)
        if left+1 < right_bak:
            Solution.QuickSort(nums, left+1, right_bak)

    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 方法一：自己写的快排，可能有问题
        '''
        137/137 cases passed (186 ms)
        Your runtime beats 5.11 % of python3 submissions
        Your memory usage beats 91.72 % of python3 submissions (17.8 MB)
        '''
        # for i in range(len(nums)):
        #     nums[i] = nums[i]**2
        # left = 0
        # right = len(nums) - 1
        # Solution.QuickSort(nums, left, right)
        # return nums

        # 方法二：调用内置函数sort()
        # '''
        # 137/137 cases passed (47 ms)
        # Your runtime beats 79.77 % of python3 submissions
        # Your memory usage beats 89.41 % of python3 submissions (17.9 MB)
        # '''
        # for i in range(len(nums)):
        #     nums[i] = nums[i]**2
        # nums.sort()
        # return nums


        # 方法三：双指针法
        left, right = 0, len(nums) - 1
        i = len(nums) - 1
        res = [0] * len(nums)
        while left <= right:
            if nums[right] ** 2 >= nums[left] ** 2:
                res[i] = nums[right] ** 2
                right -= 1
                i -= 1
            else:
                res[i] = nums[left] ** 2
                left += 1
                i -= 1
        return res
                
            
# @lc code=end

