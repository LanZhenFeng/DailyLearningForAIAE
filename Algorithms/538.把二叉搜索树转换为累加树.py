#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        215/215 cases passed (42 ms)
        Your runtime beats 96.53 % of python3 submissions
        Your memory usage beats 49.71 % of python3 submissions (18.6 MB)
        '''
        cumsum = 0

        def traversal(cur_node):
            if not cur_node: return None
            nonlocal cumsum
            if cur_node.right:
                traversal(cur_node.right)
            cumsum += cur_node.val
            cur_node.val = cumsum
            if cur_node.left:
                traversal(cur_node.left)

        traversal(root)

        return root


# @lc code=end
