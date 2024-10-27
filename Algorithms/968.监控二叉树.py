#
# @lc app=leetcode.cn id=968 lang=python3
#
# [968] 监控二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # 贪婪 + 状态记录
        # 0 该节点未被监控
        # 1 该节点放置了摄像头
        # 2 该节点已被监控
        '''
        171/171 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 16.86 % of python3 submissions (16.9 MB)
        '''
        numCamera = 0

        def traversal(node):
            if not node: return 2
            left = traversal(node.left)
            right = traversal(node.right)
            if left == 2 and right == 2:
                return 0
            elif left == 0 or right == 0:
                nonlocal numCamera
                numCamera += 1
                return 1
            else:
                return 2

        if traversal(root) == 0:
            numCamera += 1
        return numCamera


# @lc code=end
