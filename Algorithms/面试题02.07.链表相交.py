# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 41 / 45 个通过的测试用例 超出时间限制
        # if not headA or not headB:
        #     return None
        # pB = ListNode(-1)
        # pB.next = headB
        # while pB.next:
        #     pB = pB.next
        #     pA = ListNode(-1)
        #     pA.next = headA
        #     while pA.next:
        #         pA = pA.next
        #         if pA.val == pB.val and id(pA) == id(pB):
        #             return pA
        # return None

        # 
        '''
        45/45 cases passed (73 ms)
        Your runtime beats 98.77 % of python3 submissions
        Your memory usage beats 32.97 % of python3 submissions (26.84 MB)
        '''
        if not headA or not headB:
            return None
        idsA = []
        idsB = []
        pA = headA
        while pA:
            idsA.append(pA)
            pA = pA.next
        pB = headB
        while pB:
            idsB.append(pB)
            pB = pB.next
        size = min(len(idsA), len(idsB))
        if idsA[-1] != idsB[-1]:
            return None
        if idsA[-size] == idsB[-size]:
            return idsA[-size]
        for i in range(-2, -size-1, -1):
            if idsA[i] != idsB[i] and idsA[i+1] == idsB[i+1]:
                return idsA[i+1]
