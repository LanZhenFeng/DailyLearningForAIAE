#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#


# @lc code=start
class Solution:

    def fib(self, n: int) -> int:
        # 递归
        # 时间复杂度 O(2^n)
        # 空间复杂度 O(n) 系统栈空间
        '''
        31/31 cases passed (217 ms)
        Your runtime beats 20.62 % of python3 submissions
        Your memory usage beats 6.22 % of python3 submissions (16.5 MB)
        '''
        # if n == 0: return 0
        # if n == 1: return 1
        # if n == 2: return 1
        # return self.fib(n-1)+self.fib(n-2)

        # 动态规划 版本一
        # 时间复杂度 O(n)
        # 空间复杂度 O(n) dp table
        '''
        31/31 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 74.95 % of python3 submissions (16.3 MB)
        '''
        # dp = [0, 1]
        # for i in range(2, n + 1):
        #     dp.append(dp[-1] + dp[-2])
        # return dp[n]

        # 动态规划 版本一
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        '''
        31/31 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 51.56 % of python3 submissions (16.4 MB)
        '''
        dp_1, dp_2 = 0, 1
        for i in range(2, n + 1):
            dp_1, dp_2 = dp_2, dp_1+dp_2
        return dp_2 if n != 0 else dp_1


# @lc code=end
