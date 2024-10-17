#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def trimBST(self, root: Optional[TreeNode], low: int,
                high: int) -> Optional[TreeNode]:
        # 递归
        '''
        78/78 cases passed (40 ms)
        Your runtime beats 91.04 % of python3 submissions
        Your memory usage beats 13.97 % of python3 submissions (19.9 MB)
        '''
        def traversal(root, low, high):
            if not root: return None
            if root.val < low: return traversal(root.right, low, high)
            if root.val > high: return traversal(root.left, low, high)
            if root.left: root.left = traversal(root.left, low, high)
            if root.right: root.right = traversal(root.right, low, high)

            return root

        return traversal(root, low, high)


# @lc code=end
