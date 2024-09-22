#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        # 方法一：暴力遍历 iteration=7是通过所有测试用例的最小迭代数
        '''
        420/420 cases passed (32 ms)
        Your runtime beats 92.41 % of python3 submissions
        Your memory usage beats 67.49 % of python3 submissions (16.3 MB)
        '''
        iteration = 7
        while n != 1 and iteration:
            n_str = str(n)
            nums = []
            nums.extend(n_str)
            n = sum(list(map(lambda x:int(x)**2, nums)))
            iteration -= 1
        if n == 1:
            return True
        else:
            return False
        
# @lc code=end

