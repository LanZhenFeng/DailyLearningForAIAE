#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 递归
        '''
        199/199 cases passed (27 ms)
        Your runtime beats 98.86 % of python3 submissions
        Your memory usage beats 12.4 % of python3 submissions (16.5 MB)
        '''

        # flag = True

        # def is_symmetric(left, right):
        #     nonlocal flag
        #     if not left and not right:
        #         return
        #     if not left and right:
        #         flag = False
        #         return
        #     if not right and left:
        #         flag = False
        #         return
        #     if left.val != right.val:
        #         flag = False
        #         return
        #     is_symmetric(left.left, right.right)
        #     is_symmetric(left.right, right.left)

        # is_symmetric(root.left, root.right)
        # return flag

        # 递归，不使用flag
        '''
        199/199 cases passed (27 ms)
        Your runtime beats 98.86 % of python3 submissions
        Your memory usage beats 46.34 % of python3 submissions (16.5 MB)
        '''

        # def is_symmetric(left, right):
        #     if not left and not right:
        #         return True
        #     if not left and right:
        #         return False
        #     if not right and left:
        #         return False
        #     if left.val != right.val:
        #         return False
        #     compare1 = is_symmetric(left.left, right.right)
        #     compare2 = is_symmetric(left.right, right.left)
        #     return compare1 and compare2

        # return is_symmetric(root.left, root.right)

        # 迭代 队列
        '''
        199/199 cases passed (27 ms)
        Your runtime beats 98.86 % of python3 submissions
        Your memory usage beats 14.81 % of python3 submissions (16.5 MB)
        '''
        # if not root: return True
        # if not root.left and not root.right: return True
        # from collections import deque
        # queue = deque()
        # queue.append(root.left)
        # queue.append(root.right)
        # while queue:
        #     left = queue.popleft()
        #     right = queue.popleft()
        #     if not left and not right: continue
        #     if not left and right: return False
        #     if not right and left: return False
        #     if left and right:
        #         if left.val != right.val:
        #             return False
        #     queue.append(left.left)
        #     queue.append(right.right)
        #     queue.append(left.right)
        #     queue.append(right.left)
        # return True

        # 迭代 栈
        '''
        199/199 cases passed (31 ms)
        Your runtime beats 95.19 % of python3 submissions
        Your memory usage beats 68.63 % of python3 submissions (16.4 MB)
        '''
        # if not root: return True
        # if not root.left and not root.right: return True
        # from collections import deque
        # queue = deque()
        # queue.append(root.left)
        # queue.append(root.right)
        # while queue:
        #     left = queue.pop()
        #     right = queue.pop()
        #     if not left and not right: continue
        #     if not left and right: return False
        #     if not right and left: return False
        #     if left and right:
        #         if left.val != right.val:
        #             return False
        #     queue.append(left.left)
        #     queue.append(right.right)
        #     queue.append(left.right)
        #     queue.append(right.left)
        # return True

        # 迭代 层次遍历
        '''
        199/199 cases passed (19 ms)
        Your runtime beats 99.98 % of python3 submissions
        Your memory usage beats 44.17 % of python3 submissions (16.5 MB)
        '''
        if not root: return True
        if not root.left and not root.right: return True
        from collections import deque
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            size = len(queue)
            if size % 2 != 0:
                return False

            vals = []
            for i in range(size):
                node = queue.popleft()
                if node:
                    vals.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    vals.append(None)
            if vals != vals[::-1]:
                return False
        return True


# @lc code=end
