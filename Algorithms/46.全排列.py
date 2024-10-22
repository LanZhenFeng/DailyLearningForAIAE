#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 回溯
        '''
        26/26 cases passed (3 ms)
        Your runtime beats 98.88 % of python3 submissions
        Your memory usage beats 37.65 % of python3 submissions (16.7 MB)
        '''
        def backtracking(nums, path, ans, used):
            if len(path) == len(nums):
                ans.append(path[:])
                return 
            
            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                path.append(nums[i])
                backtracking(nums, path, ans, used)
                path.pop()
                used.remove(nums[i])

        ans = []
        used = set()
        backtracking(nums, [], ans, used)
        return ans
# @lc code=end

