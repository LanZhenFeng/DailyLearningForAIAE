#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def mergeTrees(self, root1: Optional[TreeNode],
                   root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 递归 前序
        '''
        182/182 cases passed (48 ms)
        Your runtime beats 84.05 % of python3 submissions
        Your memory usage beats 86.62 % of python3 submissions (16.6 MB)
        '''

        # def traversal(node1, node2):
        #     if node1 and node2:
        #         node1.val += node2.val
        #     if node1.left and node2.left:
        #         traversal(node1.left, node2.left)
        #     if not node1.left and node2.left:
        #         node1.left = node2.left
        #     if node1.right and node2.right:
        #         traversal(node1.right, node2.right)
        #     if not node1.right and node2.right:
        #         node1.right = node2.right

        # if not root1: return root2
        # if not root2: return root1
        # traversal(root1, root2)
        # return root1

        # 递归 前序 版本2
        '''
        182/182 cases passed (48 ms)
        Your runtime beats 84.05 % of python3 submissions
        Your memory usage beats 14.87 % of python3 submissions (16.8 MB)
        '''
        # if not root1: return root2
        # if not root2: return root1
        # root1.val += root2.val
        # root1.left = self.mergeTrees(root1.left, root2.left)
        # root1.right = self.mergeTrees(root1.right, root2.right)
        # return root1

        # 递归 前序 版本3
        '''
        182/182 cases passed (51 ms)
        Your runtime beats 73.21 % of python3 submissions
        Your memory usage beats 5.44 % of python3 submissions (16.9 MB)
        '''
        # if not root1: return root2
        # if not root2: return root1
        # root = TreeNode(root1.val + root2.val)
        # root.left = self.mergeTrees(root1.left, root2.left)
        # root.right = self.mergeTrees(root1.right, root2.right)
        # return root

        # 递归 中序
        '''
        182/182 cases passed (47 ms)
        Your runtime beats 87.56 % of python3 submissions
        Your memory usage beats 68.14 % of python3 submissions (16.7 MB)
        '''
        # if not root1: return root2
        # if not root2: return root1
        # root1.left = self.mergeTrees(root1.left, root2.left)
        # root1.val += root2.val
        # root1.right = self.mergeTrees(root1.right, root2.right)
        # return root1

        # 递归 后序
        '''
        182/182 cases passed (43 ms)
        Your runtime beats 96.16 % of python3 submissions
        Your memory usage beats 94.37 % of python3 submissions (16.5 MB)
        '''
        # if not root1: return root2
        # if not root2: return root1
        # root1.left = self.mergeTrees(root1.left, root2.left)
        # root1.right = self.mergeTrees(root1.right, root2.right)
        # root1.val += root2.val
        # return root1

        # 迭代
        '''
        182/182 cases passed (47 ms)
        Your runtime beats 87.56 % of python3 submissions
        Your memory usage beats 25.97 % of python3 submissions (16.8 MB)
        '''
        if not root1: return root2
        if not root2: return root1
        from collections import deque
        queue = deque()
        queue.append(root1)
        queue.append(root2)

        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            if node1.left and node2.left:
                queue.append(node1.left)
                queue.append(node2.left)
            if node1.right and node2.right:
                queue.append(node1.right)
                queue.append(node2.right)
            node1.val += node2.val
            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right
        return root1


# @lc code=end
