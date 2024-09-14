#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
from typing import List
# @lc code=start
class Solution:
    def OneCycleByClockwise(start_value, nums, n, row, col):
        # 开辟全0矩阵，再递归修改值
        ''' 
        20/20 cases passed (33 ms)
        Your runtime beats 84.68 % of python3 submissions
        Your memory usage beats 73.49 % of python3 submissions (16.4 MB)
        '''
        if n == 1:
            nums[row][col] = start_value
        elif n == 2:
            nums[row][col] = start_value
            nums[row][col+1] = start_value+1
            nums[row+1][col] = start_value+3
            nums[row+1][col+1] = start_value+2
        else:
            times = 4*(n-1)
            t = 0
            i, j = 0, 0
            while i == 0 and j <= n-1:
                nums[row+i][col+j] = start_value + t
                j += 1
                t += 1
            j -= 1
            i += 1
            while j == n-1 and i <= n-1:
                nums[row+i][col+j] = start_value + t
                i += 1
                t += 1
            i -= 1
            j -= 1
            while i == n-1 and j >= 0:
                nums[row+i][col+j] = start_value + t
                j -= 1
                t += 1
            j += 1
            i -= 1
            while j == 0 and i > 0:
                nums[row+i][col+j] = start_value + t
                i -= 1
                t += 1
            Solution.OneCycleByClockwise(times+start_value, nums, n-2, row+1, col+1)

    def generateMatrix(self, n: int) -> List[List[int]]:
        ans =[[0 for _ in range(n)] for _ in range(n)]
        Solution.OneCycleByClockwise(1, ans, n, 0, 0)
        return ans
# @lc code=end

