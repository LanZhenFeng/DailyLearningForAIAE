#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#


# @lc code=start
class Solution:

    def jump(self, nums: List[int]) -> int:
        # 贪心
        '''
        110/110 cases passed (7 ms)
        Your runtime beats 98.8 % of python3 submissions
        Your memory usage beats 68.29 % of python3 submissions (17.2 MB)
        '''
        cur_cover = 0
        next_cover = 0
        step = 0
        if len(nums) == 1: return 0
        for i in range(len(nums)):
            next_cover = max(next_cover, i + nums[i])
            if i == cur_cover:
                cur_cover = next_cover
                step += 1
                if cur_cover >= len(nums) - 1: break
        return step

        # DP
        # 时间复杂度 O(n^2)
        # 空间复杂度 O(n)
        # dp = [float("inf")] * len(nums)
        # dp[0] = 0
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if j+nums[j] >= i:
        #             dp[i] = min(dp[i], dp[j]+1)
        # return dp[-1]

        # DP+贪心
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        dp = [float("inf")] * len(nums)
        dp[0] = 0
        j = 0
        for i in range(1, len(nums)):
            while j+nums[j] < i:
                j += 1
            dp[i] = dp[j] + 1
        return dp[-1]


        # 贪心
        # 时间复杂度: O(n) 
        # 空间复杂度: O(1)
        # if len(nums) == 1: return 0
        # cur_dist = 0
        # next_dist = 0
        # count = 0
        # i = 0
        # while i < len(nums)-1:
        #     next_dist = max(next_dist, i + nums[i])
        #     if i == cur_dist:
        #         count += 1
        #         cur_dist = next_dist
        #     i += 1
        # return count

        # 反向查找出发位置
        # 时间复杂度: O(n^2) 
        # 空间复杂度: O(1)
        pos = len(nums) - 1
        steps = 0
        while pos > 0:
            for i in range(pos):
                if i+nums[i] >= pos:
                    pos = i
                    steps += 1
                    break
        return steps


# @lc code=end
