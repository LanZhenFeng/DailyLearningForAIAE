#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#


# @lc code=start
class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        # 动态规划 版本一
        # 时间复杂度 O(m × n)
        # 空间复杂度 O(m × n)
        '''
        63/63 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 32.7 % of python3 submissions (16.5 MB)
        '''
        # dp = [[0] * n for _ in range(m)]

        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 or j == 0:
        #             dp[i][j] = 1
        #         else:
        #             dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # return dp[-1][-1]

        # 动态规划 版本二
        # 时间复杂度 O(m × n)
        # 空间复杂度 O(m × n)
        '''
        63/63 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 48.82 % of python3 submissions (16.4 MB)
        '''
        # dp = [[1] * n for _ in range(m)]

        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 or j == 0:
        #             continue
        #         else:
        #             dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # return dp[-1][-1]

        # 动态规划 版本三 一维数组
        # 时间复杂度 O(m × n)
        # 空间复杂度 O(n)
        '''
        63/63 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 91.92 % of python3 submissions (16.3 MB)
        '''
        # dp = [1] * n

        # for j in range(1, m):
        #     for i in range(1, n):
        #         dp[i] += dp[i - 1]

        # return dp[-1]

        # 深度搜索
        # 时间复杂度 O(2^(m + n - 1) - 1)
        # 空间复杂度 O(m + n - 1)
        '''
        Runtime Error
        RecursionError: maximum recursion depth exceeded
        '''
        # if n == 1 and m == 1: return 1
        # return self.uniquePaths(m, n - 1) + self.uniquePaths(m - 1, n)

        # 数论
        '''
        63/63 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 39.79 % of python3 submissions (16.5 MB)
        '''
        if m == 1:
            return 1
        numerator, denominator = m + n - 2, 1
        ans = 1
        for i in range(m - 1):
            ans *= numerator / denominator
            numerator -= 1
            denominator += 1
        return round(ans)


# @lc code=end
