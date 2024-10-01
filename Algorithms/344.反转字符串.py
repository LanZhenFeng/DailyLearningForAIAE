#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 双指针
        '''
        477/477 cases passed (41 ms)
        Your runtime beats 71.19 % of python3 submissions
        Your memory usage beats 36.27 % of python3 submissions (21.7 MB)
        '''
        i = 0
        j = len(s) - 1
        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1

# @lc code=end

