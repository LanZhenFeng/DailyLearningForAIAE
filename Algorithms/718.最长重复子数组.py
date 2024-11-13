#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#


# @lc code=start
class Solution:

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # DP 2维
        # 时间复杂度：O(n × m)，n 为A长度，m为B长度
        # 空间复杂度：O(n × m)
        '''
        55/55 cases passed (1040 ms)
        Your runtime beats 89.69 % of python3 submissions
        Your memory usage beats 30.15 % of python3 submissions (41 MB)
        '''
        # dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        # res = 0
        # for i in range(1, len(nums1) + 1):
        #     for j in range(1, len(nums2) + 1):
        #         if nums1[i - 1] == nums2[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1] + 1
        #         # if dp[i][j] > res: res = dp[i][j]
        #     res = max(max(dp[i]), res)
        #     # print(i, j, dp)
        # return res

        # DP 1维
        # 时间复杂度：O(n × m)，n 为A长度，m为B长度
        # 空间复杂度：O(m)
        '''
        55/55 cases passed (825 ms)
        Your runtime beats 96.4 % of python3 submissions
        Your memory usage beats 91.92 % of python3 submissions (16.6 MB)
        '''
        dp = [0] * (len(nums2) + 1)
        res = 0
        for i in range(1, len(nums1) + 1):
            for j in range(len(nums2), 0, -1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = dp[j - 1] + 1
                else:
                    dp[j] = 0
                # if dp[i][j] > res: res = dp[i][j]
            res = max(max(dp), res)
            # print(i, j, dp)
        return res


# @lc code=end
