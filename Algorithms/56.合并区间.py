#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#


# @lc code=start
class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 贪心
        '''
        171/171 cases passed (3 ms)
        Your runtime beats 92.62 % of python3 submissions
        Your memory usage beats 6.48 % of python3 submissions (20.5 MB)
        '''
        # intervals.sort(key=lambda x: x[0])
        # new_intervals = []
        # l = intervals[0][0]
        # r = intervals[0][1]
        # for i in range(1, len(intervals)):
        #     if intervals[i][0] <= r:
        #         r = max(r, intervals[i][1])
        #     else:
        #         new_intervals.append([l, r])
        #         l = intervals[i][0]
        #         r = intervals[i][1]
        # new_intervals.append([l, r])
        # return new_intervals

        # 贪心 版本二
        '''
        171/171 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 53.53 % of python3 submissions (19.7 MB)
        '''
        intervals.sort(key=lambda x: x[0])
        new_intervals = []
        new_intervals.append(intervals[0])
        for i in range(1, len(intervals)):
            temp = intervals[i]
            if temp[0] > new_intervals[-1][1]:
                new_intervals.append(temp)
            else:
                if temp[1] > new_intervals[-1][1]:
                    new_intervals[-1][1] = temp[1]
        return new_intervals


# @lc code=end
