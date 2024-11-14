#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#


# @lc code=start
class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调栈
        # NOTE 注意开头和结尾加0
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        '''
        99/99 cases passed (103 ms)
        Your runtime beats 97.49 % of python3 submissions
        Your memory usage beats 96.35 % of python3 submissions (27.4 MB)
        '''
        res = 0
        st = []
        st.append(0)
        heights.insert(0, 0)
        heights.append(0)
        for i in range(1, len(heights)):
            if heights[i] > heights[st[-1]]:
                st.append(i)
            elif heights[i] == heights[st[-1]]:
                st.pop()
                st.append(i)
            else:
                while st and heights[i] < heights[st[-1]]:
                    mid = st.pop()
                    if st:
                        h = heights[mid]
                        w = i - st[-1] - 1
                        res = max(res, h * w)
                st.append(i)
        return res


# @lc code=end
