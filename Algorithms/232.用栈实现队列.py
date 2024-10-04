#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:
    # list 
    def __init__(self):
        self.stack1 = [] # 主栈
        self.stack2 = [] # 辅助栈
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

