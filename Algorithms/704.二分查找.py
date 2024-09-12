#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1
# @lc code=end

