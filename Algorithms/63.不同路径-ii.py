#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#


# @lc code=start
class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 动态规划 版本一
        # 时间复杂度 O(m × n)
        # 空间复杂度 O(m × n)
        '''
        41/41 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 79.48 % of python3 submissions (16.4 MB)
        '''
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        # dp = [[0] * n for _ in range(m)]

        # dp[0][0] = 0 if obstacleGrid[0][0] else 1
        # for i in range(1, m):
        #     if obstacleGrid[i][0]:
        #         dp[i][0] = 0
        #     else:
        #         dp[i][0] = dp[i - 1][0]
        # for j in range(1, n):
        #     if obstacleGrid[0][j]:
        #         dp[0][j] = 0
        #     else:
        #         dp[0][j] = dp[0][j - 1]

        # for i in range(1, m):
        #     for j in range(1, n):
        #         if obstacleGrid[i][j]:
        #             dp[i][j] = 0
        #         else:
        #             dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # return dp[-1][-1]

        # 动态规划 版本一
        # 时间复杂度 O(m × n)
        # 空间复杂度 O(n)
        '''
        41/41 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 74.26 % of python3 submissions (16.5 MB)
        '''
        # if obstacleGrid[0][0]: return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0] * n

        dp[0] = 0 if obstacleGrid[0][0] else 1
        for i in range(1, n):
            if obstacleGrid[0][i]:
                dp[i] = 0
            else:
                dp[i] = dp[i - 1]
        for j in range(1, m):
            dp[0] = 0 if obstacleGrid[j][0] else dp[0]
            for i in range(1, n):
                if obstacleGrid[j][i]:
                    dp[i] = 0
                else:
                    dp[i] += dp[i - 1]
        return dp[-1]


# @lc code=end
