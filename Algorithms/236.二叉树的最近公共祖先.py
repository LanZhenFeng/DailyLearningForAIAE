#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        # 取两个结点的路径，再寻找最近公共祖先
        '''
        32/32 cases passed (44 ms)
        Your runtime beats 93.53 % of python3 submissions
        Your memory usage beats 33.04 % of python3 submissions (20.8 MB)
        '''
        path1 = [root]
        path2 = [root]

        # def traversal(node, target_node, path):
        #     if node is target_node:
        #         return True
        #     if node.left:
        #         path.append(node.left)
        #         is_found = traversal(node.left, target_node, path)
        #         if is_found: return True
        #         path.pop()
        #     if node.right:
        #         path.append(node.right)
        #         is_found = traversal(node.right, target_node, path)
        #         if is_found: return True
        #         path.pop()
        #     return False

        # traversal(root, p, path1)
        # traversal(root, q, path2)

        # if path1[-1] in path2:
        #     return path1[-1]
        # if path2[-1] in path1:
        #     return path2[-1]

        # for i in range(len(path1) - 2, -1, -1):
        #     if path1[i] in path2:
        #         return path1[i]
        # return None

        # 递归
        '''
        32/32 cases passed (39 ms)
        Your runtime beats 98.65 % of python3 submissions
        Your memory usage beats 5.05 % of python3 submissions (21.7 MB)
        '''
        if root == q or root == p or root is None:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root

        if left is None:
            return right
        return left


# @lc code=end
