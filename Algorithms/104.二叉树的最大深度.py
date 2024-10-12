#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 递归+层次遍历
        '''
        39/39 cases passed (31 ms)
        Your runtime beats 98.38 % of python3 submissions
        Your memory usage beats 5.18 % of python3 submissions (17.9 MB)
        '''
        # max_depth = 0

        # def order(node: Optional[TreeNode], depth: int = 0):
        #     if node is None:
        #         return None
        #     nonlocal max_depth
        #     if depth + 1 >= max_depth:
        #         max_depth = depth + 1
        #     order(node.left, depth + 1)
        #     order(node.right, depth + 1)

        # order(root)
        # return max_depth

        # 迭代+层次遍历
        '''
        39/39 cases passed (34 ms)
        Your runtime beats 95.36 % of python3 submissions
        Your memory usage beats 95.98 % of python3 submissions (17.5 MB)
        '''
        max_depth = 0
        if not root: return 0
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            max_depth += 1
            for i in range(size):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return max_depth


# @lc code=end
