#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#


# @lc code=start
class Solution:

    def countSubstrings(self, s: str) -> int:
        # DP
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        '''
        132/132 cases passed (211 ms)
        Your runtime beats 56.25 % of python3 submissions
        Your memory usage beats 11.95 % of python3 submissions (24.3 MB)
        '''
        dp = [[False] * len(s) for _ in range(len(s))]
        count = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        count += 1
                        dp[i][j] = True
                    elif dp[i + 1][j - 1]:
                        count += 1
                        dp[i][j] = True
        return count

        # TODO 双指针


# @lc code=end
