#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 方法一： while 逆序
        '''
        59/59 cases passed (34 ms)
        Your runtime beats 79.12 % of python3 submissions
        Your memory usage beats 5.77 % of python3 submissions (16.6 MB)
        '''
        ans = 0
        i = -1
        while s[i] == ' ':
            i -= 1
        while i >= -len(s) and s[i] != ' ':
            i -= 1
            ans += 1
        return ans
    
        # 方法二： for 逆序
        '''
        59/59 cases passed (34 ms)
        Your runtime beats 79.12 % of python3 submissions
        Your memory usage beats 5.77 % of python3 submissions (16.6 MB)
        '''
        ans = 0
        i = -1
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                ans += 1
            else:
                if ans:
                    return ans
        return ans


# @lc code=end

