#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # d1 = defalutdict(int)
        # d2 = defalutdict(int)
        # for num1 in nums1:
        #     d1[num1] += 1
        # for num2 in nums2:
        #     d2[num2] += 1
        # 方法一：内置函数 set.intersection
        '''
        57/57 cases passed (30 ms)
        Your runtime beats 96.33 % of python3 submissions
        Your memory usage beats 57.5 % of python3 submissions (16.5 MB)
        '''
        set1 = set(nums1)
        set2 = set(nums2)
        intersection = set1.intersection(set2)
        return list(intersection)
        
# @lc code=end

