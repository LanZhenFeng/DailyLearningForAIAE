#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 栈
        '''
        99/99 cases passed (29 ms)
        Your runtime beats 96.63 % of python3 submissions
        Your memory usage beats 5.48 % of python3 submissions (16.6 MB)
        '''
        if len(s) % 2 != 0:
            return False
        from collections import deque
        bracketStack = deque()
        for i in s:
            if i == "(" or i == "{" or i == "[":
                bracketStack.append(i)
            if i == ")":
                if len(bracketStack) == 0:
                    return False
                if len(bracketStack) != 0 and bracketStack.pop() != "(":
                    return False
                
            if i == "}":
                if len(bracketStack) == 0:
                    return False
                if len(bracketStack) != 0 and bracketStack.pop() != "{":
                    return False
                
                
            if i == "]":
                if len(bracketStack) == 0:
                    return False
                if len(bracketStack) != 0 and bracketStack.pop() != "[":
                    return False
                
        if len(bracketStack) == 0:
            return True
        return False

# @lc code=end

