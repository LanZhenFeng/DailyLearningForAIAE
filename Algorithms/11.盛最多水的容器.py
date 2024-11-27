#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针
        # 时间复杂度 O(n) ✅
        # 空间复杂度 O(1) ✅
        i = 0
        j = len(height) - 1
        max_volume = 0
        while i < j:
            max_volume = max(max_volume,min(height[i], height[j]) * (j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_volume
# @lc code=end

