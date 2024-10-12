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
        #         if node.left: queue.append(node.left)
        #         if node.right: queue.append(node.right)
        # return max_depth

        # 递归+后序遍历(左右中)  高度->深度
        '''
        39/39 cases passed (35 ms)
        Your runtime beats 93.74 % of python3 submissions
        Your memory usage beats 44.88 % of python3 submissions (17.7 MB)
        '''

        # def getDepth(node):
        #     if not node:
        #         return 0
        #     leftDepth = getDepth(node.left)
        #     rightDepth = getDepth(node.right)
        #     depth = 1 + max(leftDepth, rightDepth)
        #     return depth

        # return getDepth(root)

        # 递归+前序遍历(中左右) 回溯
        '''
        39/39 cases passed (31 ms)
        Your runtime beats 98.38 % of python3 submissions
        Your memory usage beats 7.23 % of python3 submissions (17.8 MB)
        '''
        if not root: return 0
        ans = 1

        def getDepth(node, depth):
            nonlocal ans
            ans = ans if ans > depth else depth

            if node.left:
                depth += 1
                getDepth(node.left, depth)
                depth -= 1
            if node.right:
                depth += 1
                getDepth(node.right, depth)
                depth -= 1
            return None

        getDepth(root, 1)

        return ans


# @lc code=end
