#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:

    def maxDepth(self, root: 'Node') -> int:
        # 递归+层次遍历
        '''
        38/38 cases passed (40 ms)
        Your runtime beats 91.84 % of python3 submissions
        Your memory usage beats 21.19 % of python3 submissions (17.9 MB)
        '''
        max_depth = 0

        def order(node: 'Node', depth: int = 0):
            if node is None:
                return None
            nonlocal max_depth
            if depth + 1 >= max_depth:
                max_depth = depth + 1
            if node.children:
                for child in node.children:
                    order(child, depth + 1)

        order(root)
        return max_depth

        # 迭代+层次遍历
        '''
        38/38 cases passed (33 ms)
        Your runtime beats 99.39 % of python3 submissions
        Your memory usage beats 13.64 % of python3 submissions (17.9 MB)
        '''
        # max_depth = 0
        # if not root: return 0
        # from collections import deque
        # queue = deque()
        # queue.append(root)
        # while queue:
        #     size = len(queue)
        #     max_depth += 1
        #     for i in range(size):
        #         node = queue.popleft()
        #         if node.children:
        #             for child in node.children:
        #                 queue.append(child)

        # return max_depth

        # 递归+后序遍历(左右中)  高度->深度
        '''
        38/38 cases passed (35 ms)
        Your runtime beats 98.05 % of python3 submissions
        Your memory usage beats 59.68 % of python3 submissions (17.9 MB)
        '''

        # def getDepth(node):
        #     if not node:
        #         return 0

        #     depths = []
        #     if node.children:
        #         for child in node.children:
        #             depths.append(getDepth(child))
        #     else:
        #         depths.append(0)
        #     depth = 1 + max(depths)
        #     return depth

        # return getDepth(root)

        # 递归+前序遍历(中左右) 回溯
        '''
        38/38 cases passed (35 ms)
        Your runtime beats 98.06 % of python3 submissions
        Your memory usage beats 59.71 % of python3 submissions (17.9 MB)
        '''
        # if not root: return 0
        # ans = 1

        # def getDepth(node, depth):
        #     nonlocal ans
        #     ans = ans if ans > depth else depth
        #     if node.children:
        #         for chid in node.children:
        #             depth += 1
        #             getDepth(chid, depth)
        #             depth -= 1
        #     return None

        # getDepth(root, 1)

        # return ans


# @lc code=end
