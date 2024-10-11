#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 递归法
        '''
        71/71 cases passed (30 ms)
        Your runtime beats 94.21 % of python3 submissions
        Your memory usage beats 9.84 % of python3 submissions (16.5 MB)
        '''
        ans = []

        def traversal(root, ans):
            if root is None:
                return

            traversal(root.left, ans)
            ans.append(root.val)
            traversal(root.right, ans)

        traversal(root, ans)
        return ans


# @lc code=end
