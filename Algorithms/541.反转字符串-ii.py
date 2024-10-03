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
        # if len(s) == 1 or k == 1:
        #     return s
        # s = list(s)
        # lens = len(s)
        # i_substr = 0
        # while (i_substr+1)*2*k <= lens:
        #     i = 0
        #     j = k - 1
        #     while i < j:
        #         temp = s[i+i_substr*2*k]
        #         s[i+i_substr*2*k] = s[j+i_substr*2*k]
        #         s[j+i_substr*2*k] = temp
        #         i += 1
        #         j -= 1
        #     i_substr += 1
        # if lens - i_substr*2*k >= k:
        #     i = 0
        #     j = k - 1
        #     while i < j:
        #         temp = s[i+i_substr*2*k]
        #         s[i+i_substr*2*k] = s[j+i_substr*2*k]
        #         s[j+i_substr*2*k] = temp
        #         i += 1
        #         j -= 1
        # else:
        #     i = 0
        #     j = lens - i_substr*2*k - 1
        #     while i < j:
        #         temp = s[i+i_substr*2*k]
        #         s[i+i_substr*2*k] = s[j+i_substr*2*k]
        #         s[j+i_substr*2*k] = temp
        #         i += 1
        #         j -= 1
        # s = ''.join(s)
        # return s
        # new_str = []

        '''
        60/60 cases passed (32 ms)
        Your runtime beats 93.2 % of python3 submissions
        Your memory usage beats 59.67 % of python3 submissions (16.4 MB)
        '''
        # s = list(s)
        # def reverseSubStr(string, start, end):
        #     while start < end:
        #         string[start], string[end] = string[end], string[start]
        #         start += 1
        #         end -= 1

        # for i in range(0, len(s), 2*k):
        #     if len(s) - i < k:
        #         reverseSubStr(s, i, len(s)-1)
        #     # elif k <= len(s) - i <= 2*k:
        #     #     reverseSubStr(s, i, i+k)
        #     else:
        #         reverseSubStr(s, i, i+k-1)
        
        # return ''.join(s)

        # 双指针
        '''
        60/60 cases passed (30 ms)
        Your runtime beats 96.61 % of python3 submissions
        Your memory usage beats 16.09 % of python3 submissions (16.6 MB)
        '''
        p1 = 0
        while p1 < len(s):
            p2 = p1 + k
            s = s[:p1] + s[p1:p2][::-1] + s[p2:]
            p1 = p1 + 2*k

        return s

# @lc code=end

