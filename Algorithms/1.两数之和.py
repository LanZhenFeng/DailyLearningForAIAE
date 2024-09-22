#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        63/63 cases passed (37 ms)
        Your runtime beats 84.46 % of python3 submissions
        Your memory usage beats 8.22 % of python3 submissions (17.7 MB)
        '''
        dict1 = {}
        for i in range(len(nums)):
            dict1[nums[i]] = i
        for i in range(len(nums)):
            if (target - nums[i]) in dict1.keys():
                if i != dict1[target - nums[i]]:
                    return list((i, dict1[target - nums[i]]))
# @lc code=end

