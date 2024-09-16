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
        '''
        66/66 cases passed (37 ms)
        Your runtime beats 98.1 % of python3 submissions
        Your memory usage beats 8.77 % of python3 submissions (18.9 MB)
        '''
        if not head:
            return head
        p = head
        while p and p.val == val:
            head = head.next
            p = head
        while p:
            while p.next and p.next.val == val:
                p.next = p.next.next
            p = p.next
        return head
# @lc code=end

