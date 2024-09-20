#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 方法一 存储+遍历对比
        '''
        18/18 cases passed (604 ms)
        Your runtime beats 5.07 % of python3 submissions
        Your memory usage beats 82.6 % of python3 submissions (18.6 MB)
        '''
        # points = []
        # p = head
        # while p:
        #     if id(p) in points:
        #         return p
        #     points.append(id(p))
        #     p = p.next
        # return None

        # NOTE 方法二 双指针
        '''
        18/18 cases passed (39 ms)
        Your runtime beats 93.18 % of python3 submissions
        Your memory usage beats 81.25 % of python3 submissions (18.6 MB)
        '''
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                p1 = head
                p2 = fast
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
        return None




# @lc code=end

