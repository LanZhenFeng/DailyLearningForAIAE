#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 栈 list
        '''
        21/21 cases passed (36 ms)
        Your runtime beats 90.81 % of python3 submissions
        Your memory usage beats 5.38 % of python3 submissions (18.3 MB)
        '''
        stack = []
        for t in tokens:
            if t[0] == "-" and t[1:].isdigit() or t.isdigit():
                stack.append(int(t))
            elif t == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif t == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            # print(stack)
        return stack[0]
# @lc code=end

