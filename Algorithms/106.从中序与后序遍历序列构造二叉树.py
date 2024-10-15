#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def buildTree(self, inorder: List[int],
                  postorder: List[int]) -> Optional[TreeNode]:

        # 递归
        '''
        202/202 cases passed (103 ms)
        Your runtime beats 73.2 % of python3 submissions
        Your memory usage beats 36.12 % of python3 submissions (86.6 MB)
        '''

        # if len(postorder) == 0: return None
        # root = TreeNode(postorder[-1])
        # if len(postorder) == 1: return root

        # split_index = inorder.index(root.val)

        # root.left = self.buildTree(inorder[:split_index],
        #                            postorder[:split_index])
        # root.right = self.buildTree(inorder[split_index + 1:],
        #                             postorder[split_index:-1])
        # return root

        # 递归 版本2
        '''
        202/202 cases passed (55 ms)
        Your runtime beats 78.53 % of python3 submissions
        Your memory usage beats 96.51 % of python3 submissions (18 MB)
        '''

        def traversal(inorder: list, inbegin, inend, postorder, postbegin,
                      postend):
            if postend == postbegin: return None
            root = TreeNode(postorder[postend - 1])
            if postend - postbegin == 1: return root
            split_index = inorder.index(root.val, inbegin, inend)
            root.left = traversal(inorder, inbegin, split_index, postorder,
                                  postbegin, postbegin + split_index -
                                  inbegin)  # split_index - inbegin 等于 左边的size
            root.right = traversal(inorder, split_index + 1, inend, postorder,
                                   postbegin + split_index - inbegin,
                                   postend - 1)
            return root

        return traversal(inorder, 0, len(inorder), postorder, 0,
                         len(postorder))


# @lc code=end
