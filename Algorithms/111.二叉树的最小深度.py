#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 递归+层次遍历
        '''
        53/53 cases passed (213 ms)
        Your runtime beats 92.21 % of python3 submissions
        Your memory usage beats 66.65 % of python3 submissions (48.4 MB)
        '''
        # if not root: return 0
        # min_depth = 10000

        # def order(node: Optional[TreeNode], depth: int = 0):
        #     if not node.left and not node.right:
        #         nonlocal min_depth
        #         if depth + 1 <= min_depth:
        #             min_depth = depth + 1
        #         return None
        #     # nonlocal min_depth
        #     # if depth + 1 >= min_depth:
        #     #     max_depth = depth + 1
        #     if node.left: order(node.left, depth + 1)
        #     if node.right: order(node.right, depth + 1)

        # order(root)
        # return min_depth

        # 迭代+层次遍历
        '''
        53/53 cases passed (191 ms)
        Your runtime beats 99.73 % of python3 submissions
        Your memory usage beats 7.81 % of python3 submissions (48.6 MB)
        '''
        if not root: return 0
        min_depth = 0
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            min_depth += 1
            for i in range(size):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                if not node.left and not node.right:
                    return min_depth
        return min_depth


# @lc code=end
