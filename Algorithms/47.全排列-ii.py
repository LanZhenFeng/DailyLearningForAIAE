#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#


# @lc code=start
class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 回溯
        '''
        33/33 cases passed (5 ms)
        Your runtime beats 99 % of python3 submissions
        Your memory usage beats 33.41 % of python3 submissions (16.7 MB)
        '''

        def backtracking(nums, path, ans, used):
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if i > 0 and nums[i - 1] == nums[i] and not used[i - 1]:
                    continue
                if used[i]: continue
                # used.add(nums[i])
                used[i] = True
                path.append(nums[i])
                backtracking(nums, path, ans, used)
                path.pop()
                # used.remove(nums[i])
                used[i] = False

        ans = []
        used = [False] * len(nums)
        nums.sort()
        backtracking(nums, [], ans, used)
        return ans


# @lc code=end
