#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#


# @lc code=start
class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 回溯
        '''
        10/10 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 5.82 % of python3 submissions (16.7 MB)
        '''

        def backtracking(nums, startIndex, path, ans):
            if startIndex <= len(nums):
                ans.append(path[:])

            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                backtracking(nums, i + 1, path, ans)
                path.pop()

        ans = []
        backtracking(nums, 0, [], ans)
        return ans


# @lc code=end
