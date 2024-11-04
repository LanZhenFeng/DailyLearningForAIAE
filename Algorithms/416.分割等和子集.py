#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#


# @lc code=start
class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        # 回溯法 超时
        '''
        Time Limit Exceeded
        36/143 cases passed (N/A)
        '''
        # sums = sum(nums)
        # if sums % 2 != 0: return False

        # def backtracking(nums, start_index, path, sums):
        #     if sum(path) == sums // 2:
        #         return True
        #     for i in range(start_index, len(nums)):
        #         path.append(nums[i])
        #         if backtracking(nums, i + 1, path, sums): return True
        #         path.pop()
        #     return False

        # return backtracking(nums, 0, [], sums)

        # DP 01背包
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        '''
        143/143 cases passed (1362 ms)
        Your runtime beats 42.3 % of python3 submissions
        Your memory usage beats 53.42 % of python3 submissions (17 MB)
        '''
        # sums = sum(nums)
        # if sums % 2 != 0: return False
        # dp = [0] * (sums // 2 + 1)

        # for i in range(len(nums)):
        #     for j in range(sums // 2, nums[i] - 1, -1):
        #         dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        #     # print(i, dp)
        #     if dp[-1] == sums // 2: return True

        # return False

        # DP 01背包 版本二
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        '''
        143/143 cases passed (507 ms)
        Your runtime beats 77.51 % of python3 submissions
        Your memory usage beats 94.85 % of python3 submissions (16.4 MB)
        '''
        sums = sum(nums)
        if sums % 2 != 0: return False
        dp = [False] * (sums // 2 + 1)
        dp[0] = True

        for i in range(len(nums)):
            for j in range(sums // 2, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]

        return dp[sums // 2]


# @lc code=end
