#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#


# @lc code=start
class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtracking(nums, i + 1, path, ans)
                path.pop()
                used[i] = False

        ans = []
        used = [False] * len(nums)
        nums.sort()
        backtracking(nums, 0, [], ans)
        return ans


# @lc code=end
