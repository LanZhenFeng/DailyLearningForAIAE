#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 使用额外的数组
        # 时间复杂度 O(n+k)
        # 空间复杂度 O(k)
        # k = k % len(nums)
        # temp = nums[-k:]
        # n = len(nums)
        # for i in range(n-k-1, -1, -1):
        #     nums[i+k] = nums[i]
        
        # for i in range(k):
        #     nums[i] = temp[i]


        # 使用切片
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        # k = k % len(nums)
        # nums[:] = nums[-k:] + nums[:-k]

        # 海象表达式 + pythonic交换
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        # if k := (k % len(nums)):
        #     nums[:k], nums[k:] = nums[-k:], nums[:-k]

        # 双指针+翻转数组法
        # 时间复杂度 O(2*n)
        # 空间复杂度 O(1)
        # def reverse(nums, left, right):
        #     while left < right:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left += 1
        #         right -= 1

        # k = k % len(nums)
        # # reverse(nums, 0, len(nums)-1)
        # # reverse(nums, 0, k-1)
        # # reverse(nums, k, len(nums)-1)
        # # Step 1: Reverse the entire array
        # nums[:] = nums[::-1]
        # # Step 2: Reverse the first k elements
        # nums[:k] = nums[:k][::-1]
        # # Step 3: Reverse the rest
        # nums[k:] = nums[k:][::-1]

        
        # TODO 裴蜀定理优化/环状替换
# @lc code=end

