#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 方法一：递归
    '''
    28/28 cases passed (31 ms)
    Your runtime beats 94.74 % of python3 submissions
    Your memory usage beats 8.5 % of python3 submissions (17.7 MB)
    '''
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p_next = self.reverse(head.next)
        if p_next:
            if p_next.next:
                head.next = p_next.next
            p_next.next = head
        return head
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head = self.reverse(head)
        p = head.next
        head.next = None
        return p if p!=head else head
# @lc code=end

