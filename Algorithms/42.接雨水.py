#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#


# @lc code=start
class Solution:

    def trap(self, height: List[int]) -> int:
        # 单调栈
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        '''
        323/323 cases passed (15 ms)
        Your runtime beats 75.99 % of python3 submissions
        Your memory usage beats 10.09 % of python3 submissions (18.4 MB)
        '''
        res = 0
        st = []
        st.append(0)
        for i in range(1, len(height)):
            if height[i] < height[st[-1]]:
                st.append(i)
            elif height[i] == height[st[-1]]:
                st.append(i)
            else:
                while st and height[i] > height[st[-1]]:
                    mid = st.pop()
                    if st:
                        h = min(height[st[-1]], height[i]) - height[mid]
                        w = i - st[-1] - 1
                        res += h * w
                st.append(i)
        return res


# @lc code=end
