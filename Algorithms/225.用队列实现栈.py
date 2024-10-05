#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:
    # deque
    # 时间复杂度: pop为O(n)，top为O(n)，其他为O(1)
    # 空间复杂度: O(n)
    '''
    18/18 cases passed (32 ms)
    Your runtime beats 89.2 % of python3 submissions
    Your memory usage beats 70.04 % of python3 submissions (16.5 MB)
    '''
    # def __init__(self):
    #     from collections import deque
    #     self.queue1 = deque() # 队列1
    #     self.queue2 = deque() # 队列2
    #     self.size1 = 0
    #     self.size2 = 0

    # def push(self, x: int) -> None:
    #     if self.size1:
    #         self.queue1.append(x)
    #         self.size1 += 1
    #     elif self.size2:
    #         self.queue2.append(x)
    #         self.size2 += 1
    #     else:
    #         self.queue1.append(x)
    #         self.size1 += 1

    # def pop(self) -> int:
    #     if self.empty():
    #         return None

    #     if self.size1:
    #         while self.size1 > 1:
    #             self.queue2.append(self.queue1.popleft())
    #             self.size1 -= 1
    #             self.size2 += 1
    #         self.size1 -= 1
    #         return self.queue1.popleft()
        
    #     if self.size2:
    #         while self.size2 > 1:
    #             self.queue1.append(self.queue2.popleft())
    #             self.size2 -= 1
    #             self.size1 += 1
    #         self.size2 -= 1
    #         return self.queue2.popleft()
        
    # def top(self) -> int:
    #     return_val = self.pop()
    #     self.push(return_val)
    #     return return_val

    # def empty(self) -> bool:
    #     return self.size1 + self.size2 == 0
    
    # 优化成使用一个队列
    # 时间复杂度: pop为O(n)，top为O(n)，其他为O(1)
    # 空间复杂度: O(n)
    '''
    18/18 cases passed (22 ms)
    Your runtime beats 99.86 % of python3 submissions
    Your memory usage beats 5.25 % of python3 submissions (16.7 MB)
    '''
    def __init__(self):
        from collections import deque
        self.queue = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.size += 1

    def pop(self) -> int: # O(n)
        if self.empty():
            return None
        
        for i in range(self.size - 1):
            self.queue.append(self.queue.popleft())
        self.size -= 1
        return self.queue.popleft()

    def top(self) -> int:
        return_val = self.pop()
        self.push(return_val)
        return return_val

    def empty(self) -> bool:
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

