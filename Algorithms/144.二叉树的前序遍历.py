#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 递归法
        '''
        71/71 cases passed (31 ms)
        Your runtime beats 91.66 % of python3 submissions
        Your memory usage beats 5.87 % of python3 submissions (16.5 MB)
        '''
        # ans = []

        # def traversal(root, ans):
        #     if root is None:
        #         return

        #     ans.append(root.val)
        #     traversal(root.left, ans)
        #     traversal(root.right, ans)

        # traversal(root, ans)
        # return ans

        # 迭代法
        '''
        71/71 cases passed (34 ms)
        Your runtime beats 81.84 % of python3 submissions
        Your memory usage beats 89.64 % of python3 submissions (16.2 MB)
        '''
        # ans = []
        # if not root:
        #     return ans
        # stack = []
        # stack.append(root)
        # while len(stack):
        #     cur_node = stack.pop()
        #     ans.append(cur_node.val)
        #     if cur_node.right: stack.append(cur_node.right)
        #     if cur_node.left: stack.append(cur_node.left)
        # return ans

        # 统一风格迭代法
        '''
        71/71 cases passed (30 ms)
        Your runtime beats 93.8 % of python3 submissions
        Your memory usage beats 28.14 % of python3 submissions (16.5 MB)
        '''
        ans = []
        if not root: return ans
        stack = []
        stack.append(root)
        while stack:
            cur_node = stack.pop()
            if cur_node:
                if cur_node.right: stack.append(cur_node.right)
                if cur_node.left: stack.append(cur_node.left)
                stack.append(cur_node)
                stack.append(None)
            else:
                cur_node = stack.pop()
                ans.append(cur_node.val)

        return ans


# @lc code=end
