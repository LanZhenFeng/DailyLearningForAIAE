#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#


# @lc code=start
class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 暴力 超时
        # 时间复杂度 O(n^2)
        '''
        Time Limit Exceeded
        36/48 cases passed (N/A)
        '''
        # res = []
        # for i in range(len(temperatures)):
        #     next_height = 0
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             next_height = j - i
        #             break
        #     res.append(next_height)
        # return res

        # 单调栈
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        '''
        48/48 cases passed (97 ms)
        Your runtime beats 60.09 % of python3 submissions
        Your memory usage beats 13.88 % of python3 submissions (26.4 MB)
        '''
        res = [0] * len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            # if temperatures[i] <= temperatures[stack[-1]]:
            #     stack.append(i)
            # else:
            #     while stack and temperatures[i] > temperatures[stack[-1]]:
            #         res[stack[-1]] = i - stack[-1]
            #         stack.pop()
            #     stack.append(i)
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return res


# @lc code=end
