#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 递归法
        '''
        71/71 cases passed (32 ms)
        Your runtime beats 89.98 % of python3 submissions
        Your memory usage beats 25.25 % of python3 submissions (16.5 MB)
        '''
        ans = []

        def traversal(root, ans):
            if root is None:
                return

            traversal(root.left, ans)
            traversal(root.right, ans)
            ans.append(root.val)

        traversal(root, ans)
        return ans


# @lc code=end
