#
# @lc app=leetcode.cn id=624 lang=python3
#
# [624] 数组列表中的最大距离
#


# @lc code=start
class Solution:

    def maxDistance(self, arrays: List[List[int]]) -> int:
        # 一次扫描 利用有序性
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        max_dist = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]

        for i in range(1, len(arrays)):
            max_dist = max(
                max_dist, max(arrays[i][-1] - min_val, max_val - arrays[i][0]))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        return max_dist


# @lc code=end
