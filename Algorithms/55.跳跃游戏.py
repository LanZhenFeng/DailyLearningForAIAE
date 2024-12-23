#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#


# @lc code=start
class Solution:

    def canJump(self, nums: List[int]) -> bool:
        # 回溯 超时
        '''
        Time Limit Exceeded
        74/173 cases passed (N/A)
        '''
        # def backtracking(nums, start_index):
        #     if start_index == len(nums) - 1:
        #         return True

        #     start = len(nums) - 1 - start_index if nums[start_index] > len(
        #         nums) - 1 - start_index else nums[start_index]
        #     for i in range(start, 0, -1):
        #         if backtracking(nums, start_index + i): return True
        #     return False

        # return backtracking(nums, 0)

        # 贪心
        '''
        173/173 cases passed (19 ms)
        Your runtime beats 99.41 % of python3 submissions
        Your memory usage beats 68.61 % of python3 submissions (17.2 MB)
        '''
        # max_val = 0
        # i = 0
        # while i <= max_val and max_val <= len(nums) - 1:
        #     if i + nums[i] > max_val:
        #         max_val = i + nums[i]
        #     i += 1
        # if max_val >= len(nums) - 1: return True
        # else: return False

        # 贪心 for循环
        '''
        173/173 cases passed (24 ms)
        Your runtime beats 98.71 % of python3 submissions
        Your memory usage beats 85.27 % of python3 submissions (17.1 MB)
        '''
        cover = 0
        if len(nums) == 1: return True
        for i in range(len(nums)):
            if i <= cover:
                cover = max(i + nums[i], cover)
                if cover >= len(nums) - 1: return True
        return False


        # DP
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        dp = [False] *  len(nums)
        dp[-1] = True
        index = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if index - i <= nums[i]:
                index = i
                dp[index] = True
        return dp[0]

        # 记录最远距离
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        # max_dist = 0
        # i = 0
        # while i <= max_dist:
        #     max_dist = max(max_dist, i + nums[i])
        #     if max_dist >= len(nums) - 1:
        #         return True
        #     i += 1
        # return False

        # 倒序遍历 可达性判断
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        step = 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= step:
                step = 0
            step += 1
        
        return step == 1

# @lc code=end
