#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 方法一：使用字典
        '''
        63/63 cases passed (37 ms)
        Your runtime beats 84.46 % of python3 submissions
        Your memory usage beats 8.22 % of python3 submissions (17.7 MB)
        '''
        # dict1 = {}
        # for i in range(len(nums)):
        #     dict1[nums[i]] = i
        # for i in range(len(nums)):
        #     if (target - nums[i]) in dict1.keys():
        #         if i != dict1[target - nums[i]]:
        #             return list((i, dict1[target - nums[i]]))

        # 方法一v2：使用字典
        '''
        63/63 cases passed (23 ms)
        Your runtime beats 99.88 % of python3 submissions
        Your memory usage beats 15.55 % of python3 submissions (17.6 MB)
        '''
        # dict1 = {}
        # for i, num in enumerate(nums):  
        #     if target - num in dict1:   
        #         return [dict1[target - num], i]
        #     dict1[num] = i    

        # 方法二: 暴力破解
        '''
        63/63 cases passed (1690 ms)
        Your runtime beats 20.39 % of python3 submissions
        Your memory usage beats 92.39 % of python3 submissions (16.9 MB)
        '''
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        # 方法三: 集合
        '''
        63/63 cases passed (32 ms)
        Your runtime beats 94.73 % of python3 submissions
        Your memory usage beats 55.1 % of python3 submissions (17.4 MB)
        '''
        seen = set()             
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [nums.index(complement), i]
            seen.add(num)

        # TODO 双指针
# @lc code=end

