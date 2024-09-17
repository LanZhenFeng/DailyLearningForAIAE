#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
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
    def __init__(self):
        # head
        self.prev = None
        self.val = None
        self.next = None

    def get(self, index: int) -> int:
        p = self.next
        i = 0
        while p:
            if i == index:
                return p.val
            if i > index:
                return -1
            p = p.next
            i += 1
        return -1
 
    def addAtHead(self, val: int) -> None:
        new_node = MyLinkedList()
        new_node.val = val
        new_node.next = self.next
        new_node.prev = self
        if self.next:
            new_node.next.prev = new_node        
        self.next = new_node

    def addAtTail(self, val: int) -> None:
        new_node = MyLinkedList()
        new_node.val = val
        p = self
        while p.next:
            p = p.next
        p.next = new_node
        new_node.prev = p

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = MyLinkedList()
        new_node.val = val
        p = self
        i = -1
        while p.next:
            if i == index - 1:
                break
            p = p.next
            i += 1
        if i == index - 1:            
            new_node.next = p.next
            if new_node.next:
                new_node.next.prev = new_node
            new_node.prev = p
            p.next = new_node
        
    def deleteAtIndex(self, index: int) -> None:
        p = self
        i = -1
        while p.next:
            if i == index:
                break
            p = p.next
            i += 1
        if i == index:
            if p.next:
                p.next.prev = p.prev
            p.prev.next = p.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

