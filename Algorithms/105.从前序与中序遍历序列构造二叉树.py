#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def buildTree(self, preorder: List[int],
                  inorder: List[int]) -> Optional[TreeNode]:
        '''
        203/203 cases passed (71 ms)
        Your runtime beats 70.05 % of python3 submissions
        Your memory usage beats 96.46 % of python3 submissions (17.8 MB)
        '''

        def traversal(preorder, preorderbegin, preorderend, inorder,
                      inorderbegin, inorderend):

            if preorderbegin == preorderend: return None
            root = TreeNode(preorder[preorderbegin])
            if preorderend - preorderbegin == 1: return root

            delimiterIndex = inorder.index(root.val)
            root.left = traversal(
                preorder, preorderbegin + 1,
                preorderbegin + 1 + delimiterIndex - inorderbegin, inorder,
                inorderbegin, delimiterIndex)
            root.right = traversal(
                preorder, preorderbegin + 1 + delimiterIndex - inorderbegin,
                preorderend, inorder, delimiterIndex + 1, inorderend)
            return root

        root = traversal(preorder, 0, len(preorder), inorder, 0, len(inorder))
        return root


# @lc code=end
