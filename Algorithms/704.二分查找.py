#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#


# @lc code=start
class Solution:
    '''方法一'''
    @staticmethod
    def BinarySearch(nums, target, start, end):
        index = -1
        if end == start-1:
            return index
        mid = (end + start) // 2
        search_value = nums[mid]
        if search_value == target:
            index = mid
            return index
        elif search_value > target:
            index = Solution.BinarySearch(nums, target, start, mid-1)
            return index
        elif search_value < target:
            # print(mid, end)
            index = Solution.BinarySearch(nums, target, mid+1, end)
            return index
        return index

    def search(self, nums: List[int], target: int) -> int:
        # '''方法一'''
        # return Solution.BinarySearch(nums, target, 0, len(nums) - 1)
        '''方法二'''
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return -1
        return -1
# @lc code=end

