#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#


# @lc code=start
class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # 双指针 从前往后 两个while循环
        # 时间复杂度 O(m * n)
        # 空间复杂度 O(1)
        # i = 0
        # j = 0
        # r = m
        # while i < r and j < n:
        #     if nums1[i] <= nums2[j]:
        #         i += 1
        #     elif nums1[i] > nums2[j]:
        #         for k in range(r, i, -1):
        #             nums1[k] = nums1[k - 1]
        #         nums1[i] = nums2[j]
        #         j += 1
        #         i += 1
        #         r += 1

        # while j < n:
        #     nums1[r] = nums2[j]
        #     j += 1
        #     r += 1

        # 双指针 从后往前 两个while循环
        # 时间复杂度 O(m * n)
        # 空间复杂度 O(1)
        # i = m - 1
        # j = n - 1
        # r = m + n - 1
        # while i >= 0 or j >= 0:
        #     if i == -1:
        #         nums1[r] = nums2[j]
        #         j -= 1
        #         r -= 1
        #     elif j == -1:
        #         nums1[r] = nums1[i]
        #         i -= 1
        #         r -= 1
        #     elif nums1[i] <= nums2[j]:
        #         nums1[r] = nums2[j]
        #         j -= 1
        #         r -= 1
        #     elif nums1[i] > nums2[j]:
        #         nums1[r] = nums1[i]
        #         i -= 1
        #         r -= 1

        # 快速解法 两个while循环
        # 时间复杂度 O((m+n)log(m+n))
        # 空间复杂度 O(m+n)

        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()


# @lc code=end
