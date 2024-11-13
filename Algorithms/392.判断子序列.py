#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#


# @lc code=start
class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        # DP 版本1
        # 时间复杂度：O(n × m)，n 为A长度，m为B长度
        # 空间复杂度：O(n × m)
        '''
        20/20 cases passed (19 ms)
        Your runtime beats 15.29 % of python3 submissions
        Your memory usage beats 5.18 % of python3 submissions (17.4 MB)
        '''
        # dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        # for i in range(1, len(s) + 1):
        #     for j in range(1, len(t) + 1):
        #         if s[i - 1] == t[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1] + 1
        #         else:
        #             dp[i][j] = dp[i][j - 1]
        # # print(dp)
        # if dp[-1][-1] == len(s): return True
        # else: return False

        # NOTE DP 版本2 状态压缩
        # 时间复杂度：O(n × m)，n 为A长度，m为B长度
        # 空间复杂度：O(n × m)
        '''
        20/20 cases passed (19 ms)
        Your runtime beats 15.29 % of python3 submissions
        Your memory usage beats 5.18 % of python3 submissions (17.4 MB)
        '''
        dp = [0] * (len(s) + 1)

        for i in range(len(t)):
            for j in range(len(s), 0, -1):
                if s[j - 1] == t[i]:
                    dp[j] = dp[j - 1] + 1

        # print(dp)
        if dp[-1] == len(s): return True
        else: return False


# @lc code=end
