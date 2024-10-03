#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 暴力求解
        '''
        83/83 cases passed (29 ms)
        Your runtime beats 96.16 % of python3 submissions
        Your memory usage beats 83.31 % of python3 submissions (16.3 MB)
        '''
        # ans = -1
        # for i in range(len(haystack) - len(needle) + 1):
        #     j = 0
        #     while j < len(needle) and haystack[i] == needle[j]:
        #         i += 1
        #         j += 1
        #     if j == len(needle):
        #         ans = i - len(needle)
        #         break
        # return ans

        # KMP 算法
        '''
        83/83 cases passed (27 ms)
        Your runtime beats 97.96 % of python3 submissions
        Your memory usage beats 89.49 % of python3 submissions (16.2 MB)
        '''
        # next = [0] * len(needle)
        # for i in range(1, len(needle)):
        #     lens = next[i-1]
        #     while lens != 0 and needle[i] != needle[lens]:
        #         lens = next[lens - 1]

        #     if needle[i] == needle[lens]:
        #         next[i] = lens + 1
        # j = 0
        # for i in range(len(haystack)):
        #     while j > 0 and haystack[i] != needle[j]:
        #         j = next[j-1]
        #     if haystack[i] == needle[j]:
        #         j += 1
        #     if j == len(needle):
        #         return i + 1 - j

        # return -1

        # KMP算法 版本二
        '''
        83/83 cases passed (27 ms)
        Your runtime beats 97.96 % of python3 submissions
        Your memory usage beats 20.62 % of python3 submissions (16.5 MB)
        '''
        len_needle = len(needle)
        needle = [needle, haystack]
        needle = '#'.join(needle)
        next = [0] * len(needle)
        for i in range(1, len(needle)):
            lens = next[i-1]
            while lens != 0 and needle[i] != needle[lens]:
                lens = next[lens - 1]

            if needle[i] == needle[lens]:
                next[i] = lens + 1
                if next[i] == len_needle:
                    return i - 2*len_needle

        return -1

# @lc code=end

