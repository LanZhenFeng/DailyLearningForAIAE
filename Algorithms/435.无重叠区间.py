#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#


# @lc code=start
class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 贪心 版本一 判定右边界 从前往后遍历
        '''
        59/59 cases passed (60 ms)
        Your runtime beats 95.71 % of python3 submissions
        Your memory usage beats 43.42 % of python3 submissions (49.7 MB)
        '''
        remove = 0
        intervals.sort(key=lambda x: x[1])
        pr = -float('inf')
        for sl, sr in intervals:
            if sl < pr:
                remove += 1
            else:
                pr = sr
        return remove

        # 贪心 版本二 判定左边界 从后往前遍历
        '''
        59/59 cases passed (76 ms)
        Your runtime beats 70 % of python3 submissions
        Your memory usage beats 5.84 % of python3 submissions (50 MB)
        '''
        remove = 0
        intervals.sort(key=lambda x: x[0])
        pl = float('inf')
        for i in range(len(intervals) - 1, -1, -1):
            if intervals[i][1] > pl:
                remove += 1
            else:
                pl = intervals[i][0]
        return remove


# @lc code=end
