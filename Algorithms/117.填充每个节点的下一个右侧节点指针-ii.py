#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:

    def connect(self, root: 'Node') -> 'Node':
        # 递归+层次遍历
        '''
        55/55 cases passed (38 ms)
        Your runtime beats 94.08 % of python3 submissions
        Your memory usage beats 9.38 % of python3 submissions (17.6 MB)
        '''
        # l = []

        # def order(node, l, depth=0):
        #     if node is None:
        #         return None
        #     if len(l) == depth and node:
        #         l.append(node)
        #     if len(l) > depth and l[depth] is not node:
        #         last_node = l[depth]
        #         last_node.next = node
        #         l[depth] = node
        #     order(node.left, l, depth + 1)
        #     order(node.right, l, depth + 1)

        # order(root, l)
        # return root

        # 迭代+层次遍历
        '''
        55/55 cases passed (38 ms)
        Your runtime beats 94.08 % of python3 submissions
        Your memory usage beats 84.12 % of python3 submissions (17.3 MB)
        '''
        from collections import deque
        if not root: return root
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            last_node = None
            for i in range(size):
                if last_node:
                    cur_node = queue.popleft()
                    last_node.next = cur_node
                    last_node = cur_node
                else:
                    last_node = queue.popleft()
                if last_node.left: queue.append(last_node.left)
                if last_node.right: queue.append(last_node.right)

        return root


# @lc code=end
