#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListNode_w_prev:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    
class MyLinkedList:
    # 单链表
    '''
    66/66 cases passed (127 ms)
    Your runtime beats 22.4 % of python3 submissions
    Your memory usage beats 84.06 % of python3 submissions (17 MB)
    '''
    # def __init__(self):
    #     # head
    #     self.val = None
    #     self.next = None

    # def get(self, index: int) -> int:
    #     p = self.next
    #     i = 0
    #     while p:
    #         if i == index:
    #             return p.val
    #         if i > index:
    #             return -1
    #         p = p.next
    #         i += 1
    #     return -1
 
    # def addAtHead(self, val: int) -> None:
    #     new_node = MyLinkedList()
    #     new_node.val = val
    #     new_node.next = self.next
    #     self.next = new_node

    # def addAtTail(self, val: int) -> None:
    #     new_node = MyLinkedList()
    #     new_node.val = val
    #     p = self
    #     while p.next:
    #         p = p.next
    #     p.next = new_node

    # def addAtIndex(self, index: int, val: int) -> None:
    #     new_node = MyLinkedList()
    #     new_node.val = val
    #     p = self
    #     i = -1
    #     while p.next:
    #         if i == index - 1:
    #             break
    #         p = p.next
    #         i += 1
    #     if i == index - 1:            
    #         new_node.next = p.next
    #         p.next = new_node
        
    # def deleteAtIndex(self, index: int) -> None:
    #     p = self
    #     i = -1
    #     while p.next:
    #         if i == index - 1:
    #             break
    #         p = p.next
    #         i += 1
    #     if p.next:
    #         p.next = p.next.next
    
    # 双链表
    '''
    66/66 cases passed (136 ms)
    Your runtime beats 14.08 % of python3 submissions
    Your memory usage beats 5 % of python3 submissions (18 MB)
    '''
    # def __init__(self):
    #     # head
    #     self.prev = None
    #     self.val = None
    #     self.next = None

    # def get(self, index: int) -> int:
    #     p = self.next
    #     i = 0
    #     while p:
    #         if i == index:
    #             return p.val
    #         if i > index:
    #             return -1
    #         p = p.next
    #         i += 1
    #     return -1
 
    # def addAtHead(self, val: int) -> None:
    #     new_node = MyLinkedList()
    #     new_node.val = val
    #     new_node.next = self.next
    #     new_node.prev = self
    #     if self.next:
    #         new_node.next.prev = new_node        
    #     self.next = new_node

    # def addAtTail(self, val: int) -> None:
    #     new_node = MyLinkedList()
    #     new_node.val = val
    #     p = self
    #     while p.next:
    #         p = p.next
    #     p.next = new_node
    #     new_node.prev = p

    # def addAtIndex(self, index: int, val: int) -> None:
    #     new_node = MyLinkedList()
    #     new_node.val = val
    #     p = self
    #     i = -1
    #     while p.next:
    #         if i == index - 1:
    #             break
    #         p = p.next
    #         i += 1
    #     if i == index - 1:            
    #         new_node.next = p.next
    #         if new_node.next:
    #             new_node.next.prev = new_node
    #         new_node.prev = p
    #         p.next = new_node
        
    # def deleteAtIndex(self, index: int) -> None:
    #     p = self
    #     i = -1
    #     while p.next:
    #         if i == index:
    #             break
    #         p = p.next
    #         i += 1
    #     if i == index:
    #         if p.next:
    #             p.next.prev = p.prev
    #         p.prev.next = p.next
    
    # 以上方法实例化MyLinkedList作为各个结点，可能导致额外的计算开销（时间和空间）？？？
    # 下面使用ListNode来完成
    
    # 单链表
    '''
    66/66 cases passed (101 ms)
    Your runtime beats 86.57 % of python3 submissions
    Your memory usage beats 67.06 % of python3 submissions (17.1 MB)
    '''
    # def __init__(self):
    #     self.head = ListNode()
    #     self.lens = 0

    # def get(self, index: int) -> int:
    #     if index < 0 or index >= self.lens:
    #         return -1
    #     p = self.head
    #     for i in range(index+1):
    #         p = p.next
    #     return p.val
 
    # def addAtHead(self, val: int) -> None:
    #     new_node = ListNode(val, self.head.next)
    #     self.head.next = new_node
    #     self.lens += 1

    # def addAtTail(self, val: int) -> None:
    #     new_node = ListNode(val)
    #     p = self.head
    #     while p.next:
    #         p = p.next
    #     p.next = new_node
    #     self.lens += 1

    # def addAtIndex(self, index: int, val: int) -> None:
    #     if index < 0 or index > self.lens:
    #         return
    #     elif index == 0:
    #         self.addAtHead(val)
    #     elif index == self.lens:
    #         self.addAtTail(val)
    #     else:
    #         p = self.head
    #         for i in range(index):
    #             p = p.next
    #         new_node = ListNode(val, p.next)
    #         p.next = new_node
    #         self.lens += 1
        
    # def deleteAtIndex(self, index: int) -> None:
    #     if index < 0 or index >= self.lens:
    #         return
    #     p = self.head
    #     for i in range(index):
    #         p = p.next
    #     p.next = p.next.next
    #     self.lens -= 1
    
    # 双链表 循环链表
    '''
    66/66 cases passed (66 ms)
    Your runtime beats 99.17 % of python3 submissions
    Your memory usage beats 5.01 % of python3 submissions (18 MB)
    '''
    def __init__(self):
        # head
        self.SentinelNode = ListNode_w_prev(val=0)
        self.SentinelNode.prev = self.SentinelNode
        self.SentinelNode.next = self.SentinelNode
        self.lens = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.lens:
            return -1
        mid = self.lens >> 1
        # 从前往后遍历
        if index <= mid:
            p = self.SentinelNode
            for i in range(index+1):
                p = p.next
            return p.val
        else:
            p = self.SentinelNode
            for i in range(self.lens - index):
                p = p.prev
            return p.val
        
    def addAtHead(self, val: int) -> None:
        new_node = ListNode_w_prev(val)
        new_node.next = self.SentinelNode.next
        new_node.prev = self.SentinelNode
        self.SentinelNode.next.prev = new_node
        self.SentinelNode.next = new_node
        self.lens += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode_w_prev(val)
        new_node.next = self.SentinelNode
        new_node.prev = self.SentinelNode.prev
        self.SentinelNode.prev.next = new_node
        self.SentinelNode.prev = new_node
        self.lens += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.lens:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.lens:
            self.addAtTail(val)
        else:
            mid = self.lens >> 1
            if index <= mid:
                p = self.SentinelNode
                for i in range(index):
                    p = p.next
                new_node = ListNode_w_prev(val)
                new_node.next = p.next
                new_node.prev = p
                p.next.prev = new_node
                p.next = new_node
            else:
                p = self.SentinelNode
                for i in range(self.lens - index):
                    p = p.prev
                new_node = ListNode_w_prev(val)
                new_node.next = p
                new_node.prev = p.prev
                p.prev.next = new_node
                p.prev = new_node
            self.lens += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.lens:
            return
        mid = self.lens >> 1
        if index <= mid:
            p = self.SentinelNode
            for i in range(index+1):
                p = p.next
            p.next.prev = p.prev
            p.prev.next = p.next
        else:
            p = self.SentinelNode
            for i in range(self.lens - index):
                p = p.prev
            p.prev.next = p.next
            p.next.prev = p.prev
        self.lens -= 1
    


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

