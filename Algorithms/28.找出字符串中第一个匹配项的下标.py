#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        83/83 cases passed (29 ms)
        Your runtime beats 96.16 % of python3 submissions
        Your memory usage beats 83.31 % of python3 submissions (16.3 MB)
        '''
        ans = -1
        for i in range(len(haystack) - len(needle) + 1):
            j = 0
            while j < len(needle) and haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == len(needle):
                ans = i - len(needle)
                break
        return ans
# @lc code=end

