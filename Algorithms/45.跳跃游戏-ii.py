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

        # TODO 动态规划


# @lc code=end
