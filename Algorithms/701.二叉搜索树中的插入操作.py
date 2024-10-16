#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def insertIntoBST(self, root: Optional[TreeNode],
                      val: int) -> Optional[TreeNode]:

        # 递归
        '''
        35/35 cases passed (53 ms)
        Your runtime beats 99.04 % of python3 submissions
        Your memory usage beats 10.82 % of python3 submissions (18.5 MB)
        '''
        pre_node = None

        def traversal(node, val):
            nonlocal pre_node
            if not node:
                if val > pre_node.val:
                    pre_node.right = TreeNode(val)
                elif val < pre_node.val:
                    pre_node.left = TreeNode(val)
                return

            pre_node = node
            if val < node.val:
                traversal(node.left, val)
            if val > node.val:
                traversal(node.right, val)

        if not root: return TreeNode(val)
        traversal(root, val)
        return root

        # 迭代
        '''
        35/35 cases passed (61 ms)
        Your runtime beats 87.94 % of python3 submissions
        Your memory usage beats 15.45 % of python3 submissions (18.5 MB)
        '''
        if not root: return TreeNode(val)
        ptr = root
        while ptr:
            if val < ptr.val:
                if ptr.left:
                    ptr = ptr.left
                else:
                    ptr.left = TreeNode(val)
                    break
            elif val > ptr.val:
                if ptr.right:
                    ptr = ptr.right
                else:
                    ptr.right = TreeNode(val)
                    break
        return root


# @lc code=end
