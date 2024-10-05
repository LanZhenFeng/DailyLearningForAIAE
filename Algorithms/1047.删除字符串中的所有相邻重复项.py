#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:

        # 双指针
        '''
        106/106 cases passed (208 ms)
        Your runtime beats 5.18 % of python3 submissions
        Your memory usage beats 95.58 % of python3 submissions (16.9 MB)
        '''
        # i = 0
        # j = 1
        # while j < len(s):
        #     while j < len(s) and s[i] == s[j]:
        #         if i != 0:
        #             s = s[:i] + s[j+1:]
        #             i -= 1
        #             j -= 1
        #         else:
        #             s = s[j+1:]
        #     i += 1
        #     j += 1
        # return s
    
        # 栈
        '''
        106/106 cases passed (45 ms)
        Your runtime beats 99.12 % of python3 submissions
        Your memory usage beats 18.75 % of python3 submissions (17.5 MB)
        '''
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
            
# @lc code=end

