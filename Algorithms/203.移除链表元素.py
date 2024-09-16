#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 方法一：在原有链表上操作
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        '''
        66/66 cases passed (37 ms)
        Your runtime beats 98.1 % of python3 submissions
        Your memory usage beats 8.77 % of python3 submissions (18.9 MB)
        '''
        # if not head:
        #     return head
        # p = head
        # while p and p.val == val:
        #     head = head.next
        #     p = head
        # while p:
        #     while p.next and p.next.val == val:
        #         p.next = p.next.next
        #     p = p.next
        # return head

        # 方法二：设置虚拟头结点
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        '''
        66/66 cases passed (49 ms)
        Your runtime beats 61.85 % of python3 submissions
        Your memory usage beats 16.09 % of python3 submissions (18.9 MB)
        '''
        # dummy_head = ListNode(val=-1, next=head)
        # p = dummy_head
        # while p:
        #     while p.next and p.next.val == val:
        #         p.next = p.next.next
        #     p = p.next
        # return dummy_head.next

        # 方法三：递归 #NOTE 没理清递归，还需要研究
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not head:
            return head
        if head.val == val:
            return self.removeElements(head=head.next, val=val)
        else:
            head.next = self.removeElements(head=head.next, val=val)
            return head
        
# @lc code=end

