#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 方法一：迭代
        '''
        55/55 cases passed (33 ms)
        Your runtime beats 85.65 % of python3 submissions
        Your memory usage beats 5.04 % of python3 submissions (16.5 MB)
        '''
        # if not head:
        #     return head
        # dummy_head = ListNode()
        # dummy_head.next = head
        # p = dummy_head
        # while p.next and p.next.next:
        #     temp_p = p.next
        #     p.next = p.next.next
        #     temp_p.next = p.next.next
        #     p.next.next = temp_p
        #     p = p.next.next
        # return dummy_head.next
    
        # 方法二：递归
        '''
        55/55 cases passed (35 ms)
        Your runtime beats 75.7 % of python3 submissions
        Your memory usage beats 21.4 % of python3 submissions (16.5 MB)
        '''
        if not head or not head.next:
            return head

        pre = head
        cur = head.next
        next = cur.next
        
        cur.next = pre
        pre.next = self.swapPairs(next)

        return cur
# @lc code=end

