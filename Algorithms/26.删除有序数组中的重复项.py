#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 循环遍历
        # 时间复杂度 O(n^2)
        # 空间复杂度 O(1)
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1

        return len(nums)

        # 双指针 快慢指针
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        left = 0
        right = 0
        while right < len(nums):
            nums[left] = nums[right]
            right += 1
            while right < len(nums) and nums[right] == nums[left]:
                right += 1
            left += 1
        return left
# @lc code=end

