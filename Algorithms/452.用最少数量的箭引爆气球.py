#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#


# @lc code=start
class Solution:

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 暴力
        '''
        50/50 cases passed (5251 ms)
        Your runtime beats 5.15 % of python3 submissions
        Your memory usage beats 5.15 % of python3 submissions (49.6 MB)
        '''
        # min_arrow = len(points)
        # points.sort(key=lambda x: x[0])

        # used = [False] * len(points)

        # for i in range(len(points)):
        #     if used[i]: continue
        #     used[i] = True
        #     subtract = 0
        #     cur_cover = points[i]
        #     for j in range(i + 1, len(points)):
        #         next_cover = points[j]
        #         if next_cover[0] <= cur_cover[1]:
        #             cur_cover = [
        #                 max(cur_cover[0], next_cover[0]),
        #                 min(cur_cover[1], next_cover[1])
        #             ]
        #             used[j] = True
        #             subtract += 1
        #     min_arrow -= subtract
        # return min_arrow

        # 贪心
        '''
        50/50 cases passed (116 ms)
        Your runtime beats 64.71 % of python3 submissions
        Your memory usage beats 5.15 % of python3 submissions (49.6 MB)
        '''
        # points.sort(key=lambda x: x[0])
        # min_arrow = len(points)
        # i = 0
        # while i < len(points):
        #     cur_cover = points[i][1]
        #     subtract = 0
        #     while i < len(points) - 1 and points[i + 1][0] <= cur_cover:
        #         cur_cover = min(cur_cover, points[i + 1][1])
        #         i += 1
        #         subtract += 1
        #     min_arrow -= subtract
        #     i += 1

        # return min_arrow

        # 贪心 版本二 判定右边界 从前往后遍历
        # min_arrow = 0
        # points.sort(key=lambda x: x[1])
        # pr = -float('inf')
        # for sl, sr in points:
        #     if sl > pr:
        #         pr = sr
        #         min_arrow += 1
        # return min_arrow

        # 贪心 版本三 判定左边界 从后往前遍历
        min_arrow = 0
        points.sort(key=lambda x: x[0])
        pl = float('inf')
        for i in range(len(points) - 1, -1, -1):
            if points[i][1] < pl:
                min_arrow += 1
                pl = points[i][0]
        return min_arrow


# @lc code=end
