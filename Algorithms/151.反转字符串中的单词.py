#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        61/61 cases passed (47 ms)
        Your runtime beats 22.65 % of python3 submissions
        Your memory usage beats 74.05 % of python3 submissions (16.4 MB)
        '''
        ans = []
        left = 0
        right = len(s) - 1
        while s[left].isspace():
            left += 1
        while s[right].isspace():
            right -= 1
        while left <= right:
            index = right
            while left < index and not s[index-1].isspace():
                index -= 1
                # if index == left:
                #     break
            ans.append(s[index:right+1])
            while s[index-1].isspace():
                index -= 1
            right = index - 1
        return " ".join(ans)
# @lc code=end

