#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    sizes = 1
    index_NthFromEnd = 0

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 方法一：递归
        '''
        208/208 cases passed (40 ms)
        Your runtime beats 49.76 % of python3 submissions
        Your memory usage beats 79.11 % of python3 submissions (16.3 MB)
        '''
        cur_ = Solution.sizes - 1
        if head.next:
            Solution.sizes += 1
            ret = self.removeNthFromEnd(head.next, n)
        else:
            Solution.index_NthFromEnd = Solution.sizes - n
            ret = None
        if cur_ == Solution.index_NthFromEnd - 1:
            head.next = ret
        if cur_ == Solution.index_NthFromEnd:
            return ret
        else:
            return head 
        


    

# @lc code=end

