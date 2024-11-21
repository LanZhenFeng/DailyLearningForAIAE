#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 双指针
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        # if len(nums) < 2: return len(nums)
        # slow = 2
        # fast = 2
        # while fast < len(nums):
        #     if nums[fast] != nums[slow-2]:
        #         nums[slow] = nums[fast]
        #         slow += 1
        #     fast += 1

        # return slow

        # 计数
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        left = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[left] = nums[i]
                left += 1
                count = 1
            else:
                if count < 2:
                    nums[left] = nums[i]
                    left += 1
                count += 1
            # print(nums)
        return left
# @lc code=end

