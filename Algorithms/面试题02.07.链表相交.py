# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
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

        # if not headA or not headB:
        #     return None
        # idsA = []
        # idsB = []
        # pA = headA
        # while pA:
        #     idsA.append(pA)
        #     pA = pA.next
        # pB = headB
        # while pB:
        #     idsB.append(pB)
        #     pB = pB.next
        # size = min(len(idsA), len(idsB))
        # if idsA[-1] != idsB[-1]:
        #     return None
        # if idsA[-size] == idsB[-size]:
        #     return idsA[-size]
        # for i in range(-2, -size-1, -1):
        #     if idsA[i] != idsB[i] and idsA[i+1] == idsB[i+1]:
        #         return idsA[i+1]

        # 代码随想录 方法一 求长度 同时出发
        # '''
        # 45/45 cases passed (89 ms)
        # Your runtime beats 53.68 % of python3 submissions
        # Your memory usage beats 8.03 % of python3 submissions (26.93 MB)
        # '''
        # lenA, lenB = 0, 0
        # cur = headA
        # while cur:         # 求链表A的长度
        #     cur = cur.next 
        #     lenA += 1
        # cur = headB 
        # while cur:         # 求链表B的长度
        #     cur = cur.next 
        #     lenB += 1
        # curA, curB = headA, headB
        # if lenA > lenB:     # 让curB为最长链表的头，lenB为其长度
        #     curA, curB = curB, curA
        #     lenA, lenB = lenB, lenA 
        # for _ in range(lenB - lenA):  # 让curA和curB在同一起点上（末尾位置对齐）
        #     curB = curB.next 
        # while curA:         #  遍历curA 和 curB，遇到相同则直接返回
        #     if curA == curB:
        #         return curA
        #     else:
        #         curA = curA.next 
        #         curB = curB.next
        # return None 
    
    # 代码随想录 方法二 求长度，同时出发 （代码复用）
    # '''
    # 45/45 cases passed (81 ms)
    # Your runtime beats 86.01 % of python3 submissions
    # Your memory usage beats 17.50 % of python3 submissions (26.88 MB)
    # '''
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     lenA = self.getLength(headA)
    #     lenB = self.getLength(headB)
        
    #     # 通过移动较长的链表，使两链表长度相等
    #     if lenA > lenB:
    #         headA = self.moveForward(headA, lenA - lenB)
    #     else:
    #         headB = self.moveForward(headB, lenB - lenA)
        
    #     # 将两个头向前移动，直到它们相交
    #     while headA and headB:
    #         if headA == headB:
    #             return headA
    #         headA = headA.next
    #         headB = headB.next
        
    #     return None
    
    # def getLength(self, head: ListNode) -> int:
    #     length = 0
    #     while head:
    #         length += 1
    #         head = head.next
    #     return length
    
    # def moveForward(self, head: ListNode, steps: int) -> ListNode:
    #     while steps > 0:
    #         head = head.next
    #         steps -= 1
    #     return head

    # 代码随想录 方法三 求长度，同时出发 （代码复用 + 精简）
    # '''
    # 45/45 cases passed (83 ms)
    # Your runtime beats 79.37 % of python3 submissions
    # Your memory usage beats 13.02 % of python3 submissions (26.90 MB)
    # '''
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     dis = self.getLength(headA) - self.getLength(headB)
        
    #     # 通过移动较长的链表，使两链表长度相等
    #     if dis > 0:
    #         headA = self.moveForward(headA, dis)
    #     else:
    #         headB = self.moveForward(headB, abs(dis))
        
    #     # 将两个头向前移动，直到它们相交
    #     while headA and headB:
    #         if headA == headB:
    #             return headA
    #         headA = headA.next
    #         headB = headB.next
        
    #     return None
    
    # def getLength(self, head: ListNode) -> int:
    #     length = 0
    #     while head:
    #         length += 1
    #         head = head.next
    #     return length
    
    # def moveForward(self, head: ListNode, steps: int) -> ListNode:
    #     while steps > 0:
    #         head = head.next
    #         steps -= 1
    #     return head

    # NOTE 代码随想录 方法四 等比例法 很好的办法，一轮过后，两个指针指向按结尾排的同一列，
    # '''
    # 45/45 cases passed (76 ms)
    # Your runtime beats 96.11 % of python3 submissions
    # Your memory usage beats 45.73 % of python3 submissions (26.82 MB)
    # '''
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 处理边缘情况
        if not headA or not headB:
            return None
        
        # 在每个链表的头部初始化两个指针
        pointerA = headA
        pointerB = headB
        
        # 遍历两个链表直到指针相交
        while pointerA != pointerB:
            # 将指针向前移动一个节点
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        
        # 如果相交，指针将位于交点节点，如果没有交点，值为None
        return pointerA

