#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:

    def reverseStr(self, s: str, k: int) -> str:
        '''
        60/60 cases passed (44 ms)
        Your runtime beats 36.74 % of python3 submissions
        Your memory usage beats 13.05 % of python3 submissions (16.6 MB)
        '''
        if len(s) == 1 or k == 1:
            return s
        s = list(s)
        lens = len(s)
        i_substr = 0
        while (i_substr+1)*2*k <= lens:
            i = 0
            j = k - 1
            while i < j:
                temp = s[i+i_substr*2*k]
                s[i+i_substr*2*k] = s[j+i_substr*2*k]
                s[j+i_substr*2*k] = temp
                i += 1
                j -= 1
            i_substr += 1
        if lens - i_substr*2*k >= k:
            i = 0
            j = k - 1
            while i < j:
                temp = s[i+i_substr*2*k]
                s[i+i_substr*2*k] = s[j+i_substr*2*k]
                s[j+i_substr*2*k] = temp
                i += 1
                j -= 1
        else:
            i = 0
            j = lens - i_substr*2*k - 1
            while i < j:
                temp = s[i+i_substr*2*k]
                s[i+i_substr*2*k] = s[j+i_substr*2*k]
                s[j+i_substr*2*k] = temp
                i += 1
                j -= 1
        s = ''.join(s)
        return s

# @lc code=end

