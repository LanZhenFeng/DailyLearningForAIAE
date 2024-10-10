#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#


# @lc code=start
class Solution:

    def longestPalindrome(self, s: str) -> str:
        # i = 0
        # j = len(s)-1
        # start_index = None
        # end_index = None
        # while i <= j:
        #     if s[i] == s[j]:
        #         start_index = i
        #         end_index = j
        #         while i <= j and s[i] == s[j]:
        #             i += 1
        #             j -= 1
        #         if i > j:
        #             return s[start_index:end_index+1]
        #         else:
        '''
        142/142 cases passed (376 ms)
        Your runtime beats 68.99 % of python3 submissions
        Your memory usage beats 89.16 % of python3 submissions (16.3 MB)
        '''
        if len(s) == 1:
            return s
        start_index = 0
        end_index = 0
        for i in range(1, len(s)):
            j = i
            k = i
            while j >= 0 and s[j] == s[i]:
                j -= 1
            while k <= len(s) - 1 and s[k] == s[i]:
                k += 1
            while j >= 0 and k <= len(s) - 1 and s[j] == s[k]:
                j -= 1
                k += 1
            if k - j >= end_index - start_index:
                end_index = k
                start_index = j
        return s[start_index + 1:end_index]


# @lc code=end
