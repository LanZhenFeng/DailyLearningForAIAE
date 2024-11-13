#
# @lc app=leetcode.cn id=1035 lang=python3
#
# [1035] 不相交的线
#


# @lc code=start
class Solution:

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # DP 2维
        # 时间复杂度：O(n × m)，n 为A长度，m为B长度
        # 空间复杂度：O(n × m)
        '''
        74/74 cases passed (71 ms)
        Your runtime beats 94.25 % of python3 submissions
        Your memory usage beats 25.89 % of python3 submissions (17.1 MB)
        '''
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            # print(i, j, dp)
        return dp[-1][-1]

        # TODO DP 1维


# @lc code=end
