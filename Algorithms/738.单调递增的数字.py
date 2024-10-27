#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#


# @lc code=start
class Solution:

    def monotoneIncreasingDigits(self, n: int) -> int:
        # 暴力解法
        '''
        Time Limit Exceeded
        208/308 cases passed (N/A)
        '''
        # def check(n):
        #     n, lr = divmod(n, 10)
        #     while n:
        #         n, r = divmod(n, 10)
        #         if lr < r: return False
        #         lr = r

        #     return True

        # for i in range(n, 0, -1):
        #     if check(i):
        #         return i

        # return 0

        # 贪心
        '''
        308/308 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 63.62 % of python3 submissions (16.4 MB)
        '''
        # if n < 10: return n
        # digit_list = []
        # while n:
        #     n, r = divmod(n, 10)
        #     digit_list.append(r)

        # for i in range(1, len(digit_list)):
        #     if digit_list[i] > digit_list[i - 1]:
        #         digit_list[i] -= 1
        #         j = i - 1
        #         while j >= 0:
        #             digit_list[j] = 9
        #             j -= 1

        # res = digit_list[-1]
        # for i in range(len(digit_list) - 2, -1, -1):
        #     res = res * 10 + digit_list[i]

        # return res

        # 贪心 只替换一次全9
        '''
        308/308 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 20.65 % of python3 submissions (16.5 MB)
        '''
        if n < 10: return n
        digit_list = []
        while n:
            n, r = divmod(n, 10)
            digit_list.append(r)

        flag = -1
        for i in range(1, len(digit_list)):
            if digit_list[i] > digit_list[i - 1]:
                digit_list[i] -= 1
                flag = i - 1

        for i in range(flag, -1, -1):
            digit_list[i] = 9

        res = digit_list[-1]
        for i in range(len(digit_list) - 2, -1, -1):
            res = res * 10 + digit_list[i]

        return res


# @lc code=end
