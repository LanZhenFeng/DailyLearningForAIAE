#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # 迭代遍历+寻找左叶子
        '''
        100/100 cases passed (31 ms)
        Your runtime beats 94.85 % of python3 submissions
        Your memory usage beats 71.06 % of python3 submissions (16.6 MB)
        '''
        # res = []

        # stack = [root]
        # while stack:
        #     cur_ = stack.pop()
        #     if cur_.right:
        #         stack.append(cur_.right)
        #     if cur_.left:
        #         stack.append(cur_.left)
        #         if not cur_.left.left and not cur_.left.right:
        #             res.append(cur_.left.val)
        # return sum(res)

        # 递归遍历+寻找左叶子
        '''
        100/100 cases passed (27 ms)
        Your runtime beats 98.86 % of python3 submissions
        Your memory usage beats 5.08 % of python3 submissions (16.9 MB)
        '''
        res = []

        def getLeftLeaves(node, res):

            if node.left:
                if not node.left.left and not node.left.right:
                    res.append(node.left.val)
                getLeftLeaves(node.left, res)
            if node.right:
                getLeftLeaves(node.right, res)

        getLeftLeaves(root, res)

        return sum(res)


# @lc code=end
