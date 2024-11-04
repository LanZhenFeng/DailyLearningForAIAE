#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#


# @lc code=start
class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # 回溯 超时
        '''
        Time Limit Exceeded
        18/140 cases passed (N/A)
        '''
        # if sum(nums) < target: return 0
        # len_nums = len(nums)

        # def backtracking(nums, target, start_index, path, res):
        #     if len(path) == len_nums:
        #         print(path)
        #         pathSt = ''.join(path)
        #         if eval(pathSt) == target:
        #             res.append(1)
        #             return
        #     for i in range(start_index, len_nums):
        #         for sign in ["-", "+"]:
        #             path.append(sign + str(nums[i]))
        #             backtracking(nums, target, i + 1, path, res)
        #             path.pop()

        # res = []
        # backtracking(nums, target, 0, [], res)
        # return sum(res)

        # DP 01背包 2维
        # 时间复杂度：O(n × m)，n为正数个数，m为背包容量
        # 空间复杂度：O(m)，m为背包容量
        '''
        140/140 cases passed (43 ms)
        Your runtime beats 57.94 % of python3 submissions
        Your memory usage beats 29.23 % of python3 submissions (16.8 MB)
        '''
        total_sum = sum(nums)
        if total_sum < abs(target): return 0
        if (total_sum + target) % 2 != 0: return 0
        bag_size = (total_sum + target) // 2
        dp = [[0] * (bag_size + 1) for _ in range(len(nums) + 1)]

        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(bag_size + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] + dp[i - 1][j - nums[i - 1]]
        return dp[-1][-1]

        # DP 01背包 1维
        # 时间复杂度：O(n × m)，n为正数个数，m为背包容量
        # 空间复杂度：O(m)，m为背包容量
        '''
        140/140 cases passed (17 ms)
        Your runtime beats 91.35 % of python3 submissions
        Your memory usage beats 86.54 % of python3 submissions (16.4 MB)
        '''
        total_sum = sum(nums)
        if total_sum < abs(target): return 0
        if (total_sum + target) % 2 != 0: return 0
        bag_size = (total_sum + target) // 2
        dp = [0] * (bag_size + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bag_size, nums[i] - 1, -1):
                dp[j] = dp[j] + dp[j - nums[i]]
        return dp[-1]


# @lc code=end
