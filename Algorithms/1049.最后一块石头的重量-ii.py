#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#


# @lc code=start
class Solution:

    def lastStoneWeightII(self, stones: List[int]) -> int:
        # DP 01背包
        # 时间复杂度：O(m × n) , m是石头总重量（准确的说是总重量的一半），n为石头块数
        # 空间复杂度：O(m)
        '''
        90/90 cases passed (19 ms)
        Your runtime beats 73.65 % of python3 submissions
        Your memory usage beats 54.29 % of python3 submissions (16.5 MB)
        '''
        # total_sum = sum(stones)
        # target_num = total_sum // 2
        # dp = [0] * (target_num + 1)

        # for i in range(len(stones)):
        #     for j in range(target_num, stones[i] - 1, -1):
        #         dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        # return total_sum - dp[-1] - dp[-1]

        # DP 01背包
        # 时间复杂度：O(m × n) , m是石头总重量（准确的说是总重量的一半），n为石头块数
        # 空间复杂度：O(m)
        '''
        90/90 cases passed (3 ms)
        Your runtime beats 99.68 % of python3 submissions
        Your memory usage beats 55.57 % of python3 submissions (16.5 MB)
        '''
        total_sum = sum(stones)
        target_num = total_sum // 2
        dp = [False] * (target_num + 1)
        dp[0] = True

        for i in range(len(stones)):
            for j in range(target_num, stones[i] - 1, -1):
                dp[j] = dp[j] or dp[j - stones[i]]

        for i in range(target_num, -1, -1):
            if dp[i]:
                return total_sum - 2 * i

        return 0


# @lc code=end
