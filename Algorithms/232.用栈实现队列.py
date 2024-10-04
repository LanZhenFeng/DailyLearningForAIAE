#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:
    # list 
    '''
    22/22 cases passed (25 ms)
    Your runtime beats 98.97 % of python3 submissions
    Your memory usage beats 22.3 % of python3 submissions (16.6 MB)
    '''
    # def __init__(self):
    #     self.stack1 = [] # 主栈
    #     self.stack2 = [] # 辅助栈
    #     self.top = -1   # 主栈指针

    # def push(self, x: int) -> None:
    #     self.stack1.append(x)
    #     self.top += 1

    # def pop(self) -> int:
    #     if self.top != -1:
    #         for i in range(self.top):
    #             self.stack2.append(self.stack1.pop())
    #         return_val = self.stack1.pop()
    #         for i in range(self.top):
    #             self.stack1.append(self.stack2.pop())
    #         self.top -= 1
    #         return return_val

    # def peek(self) -> int:
    #     if self.top != -1:
    #         for i in range(self.top):
    #             self.stack2.append(self.stack1.pop())
    #         return_val = self.stack1.pop()
    #         self.stack1.append(return_val)
    #         for i in range(self.top):
    #             self.stack1.append(self.stack2.pop())
    #         return return_val

    # def empty(self) -> bool:
    #     return self.top == -1
    
    # deque
    '''
    22/22 cases passed (20 ms)
    Your runtime beats 100 % of python3 submissions
    Your memory usage beats 5.03 % of python3 submissions (16.7 MB)
    '''
    def __init__(self):
        from collections import deque
        self.stack1 = deque() # 主栈
        self.stack2 = deque() # 辅助栈
        self.top = -1   # 主栈指针

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.top += 1

    def pop(self) -> int:
        if self.top != -1:
            for i in range(self.top):
                self.stack2.append(self.stack1.pop())
            return_val = self.stack1.pop()
            for i in range(self.top):
                self.stack1.append(self.stack2.pop())
            self.top -= 1
            return return_val

    def peek(self) -> int:
        if self.top != -1:
            for i in range(self.top):
                self.stack2.append(self.stack1.pop())
            return_val = self.stack1.pop()
            self.stack1.append(return_val)
            for i in range(self.top):
                self.stack1.append(self.stack2.pop())
            return return_val

    def empty(self) -> bool:
        return self.top == -1



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

