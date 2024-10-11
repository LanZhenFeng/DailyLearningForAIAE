#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 递归 (前序遍历)
        '''
        77/77 cases passed (29 ms)
        Your runtime beats 96.49 % of python3 submissions
        Your memory usage beats 19.26 % of python3 submissions (16.5 MB)
        '''
        # if not root:
        #     return
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root

        # 递归 (后序遍历)
        '''
        77/77 cases passed (31 ms)
        Your runtime beats 92.45 % of python3 submissions
        Your memory usage beats 68.91 % of python3 submissions (16.4 MB)
        '''
        # if not root:
        #     return
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # root.left, root.right = root.right, root.left
        # return root

        # 递归 （非正式的中序遍历）
        '''
        77/77 cases passed (37 ms)
        Your runtime beats 68.55 % of python3 submissions
        Your memory usage beats 46.07 % of python3 submissions (16.4 MB)
        '''
        # if not root:
        #     return
        # self.invertTree(root.left)
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)

        # return root

        # 迭代 dfs 前序遍历
        '''
        77/77 cases passed (38 ms)
        Your runtime beats 60.84 % of python3 submissions
        Your memory usage beats 80.93 % of python3 submissions (16.3 MB)
        '''
        # if not root: return root
        # stack = []
        # stack.append(root)
        # while stack:
        #     cur_node = stack.pop()
        #     cur_node.left, cur_node.right = cur_node.right, cur_node.left
        #     if cur_node.right: stack.append(cur_node.right)
        #     if cur_node.left: stack.append(cur_node.left)
        # return root

        # 迭代 dfs 中序遍历
        '''
        77/77 cases passed (40 ms)
        Your runtime beats 47.83 % of python3 submissions
        Your memory usage beats 28.9 % of python3 submissions (16.5 MB)
        '''
        # if not root: return root
        # stack = []
        # stack.append(root)
        # while stack:
        #     cur_node = stack.pop()
        #     if cur_node.right: stack.append(cur_node.right)
        #     cur_node.left, cur_node.right = cur_node.right, cur_node.left
        #     if cur_node.right: stack.append(cur_node.right)

        # return root

        # 迭代 dfs 后序遍历
        '''
        77/77 cases passed (38 ms)
        Your runtime beats 60.84 % of python3 submissions
        Your memory usage beats 5.71 % of python3 submissions (16.5 MB)
        '''
        # if not root: return root
        # stack = []
        # stack.append(root)
        # while stack:
        #     cur_node = stack.pop()
        #     if cur_node.right: stack.append(cur_node.right)
        #     if cur_node.left: stack.append(cur_node.left)
        #     cur_node.left, cur_node.right = cur_node.right, cur_node.left
        # return root

        # 统一风格 迭代 dfs 中序遍历
        '''
        77/77 cases passed (28 ms)
        Your runtime beats 97.61 % of python3 submissions
        Your memory usage beats 6.74 % of python3 submissions (16.5 MB)
        '''
        # if not root: return root
        # stack = []
        # stack.append(root)
        # while stack:
        #     cur_node = stack.pop()
        #     if cur_node:
        #         if cur_node.left: stack.append(cur_node.left)
        #         stack.append(cur_node)
        #         stack.append(None)
        #         if cur_node.right: stack.append(cur_node.right)
        #     else:
        #         cur_node = stack.pop()
        #         cur_node.left, cur_node.right = cur_node.right, cur_node.left

        # return root

        # 统一风格 迭代 dfs 前序遍历
        '''
        77/77 cases passed (30 ms)
        Your runtime beats 94.89 % of python3 submissions
        Your memory usage beats 5.09 % of python3 submissions (16.6 MB)
        '''
        # if not root: return root
        # stack = []
        # stack.append(root)
        # while stack:
        #     cur_node = stack.pop()
        #     if cur_node:
        #         stack.append(cur_node)
        #         stack.append(None)
        #         if cur_node.left: stack.append(cur_node.left)
        #         if cur_node.right: stack.append(cur_node.right)
        #     else:
        #         cur_node = stack.pop()
        #         cur_node.left, cur_node.right = cur_node.right, cur_node.left

        # return root

        # 统一风格 迭代 dfs 后序遍历
        '''
        77/77 cases passed (28 ms)
        Your runtime beats 97.61 % of python3 submissions
        Your memory usage beats 10.89 % of python3 submissions (16.5 MB)
        '''

        # if not root: return root
        # stack = []
        # stack.append(root)
        # while stack:
        #     cur_node = stack.pop()
        #     if cur_node:
        #         if cur_node.left: stack.append(cur_node.left)
        #         if cur_node.right: stack.append(cur_node.right)
        #         stack.append(cur_node)
        #         stack.append(None)
        #     else:
        #         cur_node = stack.pop()
        #         cur_node.left, cur_node.right = cur_node.right, cur_node.left

        # return root

        # 递归 bfs 层次遍历
        '''
        77/77 cases passed (29 ms)
        Your runtime beats 96.44 % of python3 submissions
        Your memory usage beats 60.06 % of python3 submissions (16.4 MB)
        '''
        # def order(root):
        #     if not root: return
        #     root.left, root.right = root.right, root.left
        #     if root.left: order(root.left)
        #     if root.right: order(root.right)

        # order(root)
        # return root

        # 迭代 bfs 层次遍历
        '''
        77/77 cases passed (30 ms)
        Your runtime beats 94.89 % of python3 submissions
        Your memory usage beats 75.27 % of python3 submissions (16.3 MB)
        '''
        from collections import deque
        if not root: return root
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                node.left, node.right = node.right, node.left
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return root


# @lc code=end
