#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 栈 deque
        '''
        99/99 cases passed (29 ms)
        Your runtime beats 96.63 % of python3 submissions
        Your memory usage beats 5.48 % of python3 submissions (16.6 MB)
        '''
        # if len(s) % 2 != 0:
        #     return False
        # from collections import deque
        # bracketStack = deque()
        # for i in s:
        #     if i == "(" or i == "{" or i == "[":
        #         bracketStack.append(i)
        #     if i == ")":
        #         if len(bracketStack) == 0:
        #             return False
        #         if len(bracketStack) != 0 and bracketStack.pop() != "(":
        #             return False
                
        #     if i == "}":
        #         if len(bracketStack) == 0:
        #             return False
        #         if len(bracketStack) != 0 and bracketStack.pop() != "{":
        #             return False
                
                
        #     if i == "]":
        #         if len(bracketStack) == 0:
        #             return False
        #         if len(bracketStack) != 0 and bracketStack.pop() != "[":
        #             return False
                
        # if len(bracketStack) == 0:
        #     return True
        # return False


        # 栈 list
        '''
        99/99 cases passed (31 ms)
        Your runtime beats 92.71 % of python3 submissions
        Your memory usage beats 70.03 % of python3 submissions (16.4 MB)
        '''
        # stack = []
        
        # for item in s:
        #     if item == '(':
        #         stack.append(')')
        #     elif item == '[':
        #         stack.append(']')
        #     elif item == '{':
        #         stack.append('}')
        #     elif not stack or stack[-1] != item:
        #         return False
        #     else:
        #         stack.pop()
        
        # return True if not stack else False


        # 栈+字典
        '''
        99/99 cases passed (32 ms)
        Your runtime beats 90.48 % of python3 submissions
        Your memory usage beats 34.26 % of python3 submissions (16.4 MB)
        '''
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
            elif not stack or stack[-1] != item: 
                return False
            else: 
                stack.pop()
        return True if not stack else False

# @lc code=end

