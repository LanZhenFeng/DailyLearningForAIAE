#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def searchBST(self, root: Optional[TreeNode],
                  val: int) -> Optional[TreeNode]:
        # 迭代
        '''
        36/36 cases passed (54 ms)
        Your runtime beats 83.08 % of python3 submissions
        Your memory usage beats 72.92 % of python3 submissions (18.2 MB)
        '''
        # ptr = root
        # while ptr and val != ptr.val:
        #     if val < ptr.val:
        #         ptr = ptr.left
        #     else:
        #         ptr = ptr.right
        # return ptr

        # 递归
        '''
        36/36 cases passed (50 ms)
        Your runtime beats 93.76 % of python3 submissions
        Your memory usage beats 17.19 % of python3 submissions (18.4 MB)
        '''
        if not root: return None
        if root.val == val: return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


# @lc code=end
