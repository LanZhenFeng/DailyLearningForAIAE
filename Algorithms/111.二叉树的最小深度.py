#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 递归+层次遍历
        '''
        53/53 cases passed (213 ms)
        Your runtime beats 92.21 % of python3 submissions
        Your memory usage beats 66.65 % of python3 submissions (48.4 MB)
        '''
        # if not root: return 0
        # min_depth = 10000

        # def order(node: Optional[TreeNode], depth: int = 0):
        #     if not node.left and not node.right:
        #         nonlocal min_depth
        #         if depth + 1 <= min_depth:
        #             min_depth = depth + 1
        #         return None
        #     # nonlocal min_depth
        #     # if depth + 1 >= min_depth:
        #     #     max_depth = depth + 1
        #     if node.left: order(node.left, depth + 1)
        #     if node.right: order(node.right, depth + 1)

        # order(root)
        # return min_depth

        # 迭代+层次遍历
        '''
        53/53 cases passed (191 ms)
        Your runtime beats 99.73 % of python3 submissions
        Your memory usage beats 7.81 % of python3 submissions (48.6 MB)
        '''
        # if not root: return 0
        # min_depth = 0
        # from collections import deque
        # queue = deque()
        # queue.append(root)
        # while queue:
        #     size = len(queue)
        #     min_depth += 1
        #     for i in range(size):
        #         node = queue.popleft()
        #         if node.left: queue.append(node.left)
        #         if node.right: queue.append(node.right)
        #         if not node.left and not node.right:
        #             return min_depth
        # return min_depth

        # 递归+后序遍历(左右中)  高度->深度
        '''
        53/53 cases passed (255 ms)
        Your runtime beats 57.76 % of python3 submissions
        Your memory usage beats 57.78 % of python3 submissions (48.4 MB)
        '''

        # def getDepth(node):
        #     if not node:
        #         return 0
        #     leftDepth = getDepth(node.left)
        #     rightDepth = getDepth(node.right)
        #     if not leftDepth and rightDepth:
        #         return 1 + rightDepth
        #     elif not rightDepth and leftDepth:
        #         return 1 + leftDepth
        #     else:
        #         depth = 1 + min(leftDepth, rightDepth)
        #         return depth

        # return getDepth(root)

        # 递归+前序遍历(中左右) 回溯
        '''
        53/53 cases passed (230 ms)
        Your runtime beats 79.54 % of python3 submissions
        Your memory usage beats 28.06 % of python3 submissions (48.5 MB)
        '''
        if not root: return 0
        ans = 10000

        def getDepth(node, depth):
            nonlocal ans

            if not node.left and not node.right:
                ans = ans if ans < depth else depth

            if node.left:
                getDepth(node.left, depth + 1)
            if node.right:
                getDepth(node.right, depth + 1)

        getDepth(root, 1)

        return ans


# @lc code=end
