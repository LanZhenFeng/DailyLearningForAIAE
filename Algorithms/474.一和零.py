#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#


# @lc code=start
class Solution:

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # DP 01背包 2维
        # 时间复杂度: O(k × m × n)，k 为strs的长度
        # 空间复杂度: O(m × n)
        '''
        73/73 cases passed (1555 ms)
        Your runtime beats 82.67 % of python3 submissions
        Your memory usage beats 35.74 % of python3 submissions (16.8 MB)
        '''
        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        # for str in strs:
        #     ones = str.count('1')
        #     zeros = str.count('0')
        #     for i in range(m, zeros - 1, -1):
        #         for j in range(n, ones - 1, -1):
        #             dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        # return dp[-1][-1]

        # DP 01背包 3维
        '''
        73/73 cases passed (2406 ms)
        Your runtime beats 19.75 % of python3 submissions
        Your memory usage beats 13.34 % of python3 submissions (70.9 MB)
        '''
        dp = [[[0] * (n + 1) for _ in range(m + 1)]
              for _ in range(len(strs) + 1)]
        # print(len(dp), len(dp[0]), len(dp[0][0]))

        for i in range(1, len(strs) + 1):
            zeros = strs[i - 1].count('0')
            ones = strs[i - 1].count('1')
            for j in range(m + 1):
                for k in range(n + 1):
                    if j < zeros or k < ones:
                        # print(i, j, k)
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = max(dp[i - 1][j][k],
                                          dp[i - 1][j - zeros][k - ones] + 1)
            # print(dp[i])

        return dp[-1][-1][-1]


# @lc code=end
