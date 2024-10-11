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
        # ans = []

        # def traversal(root, ans):
        #     if root is None:
        #         return

        #     traversal(root.left, ans)
        #     traversal(root.right, ans)
        #     ans.append(root.val)

        # traversal(root, ans)
        # return ans

        # 迭代法
        '''
        71/71 cases passed (26 ms)
        Your runtime beats 98.66 % of python3 submissions
        Your memory usage beats 69.38 % of python3 submissions (16.4 MB)
        '''
        # ans = []
        # if not root:
        #     return ans
        # stack = []
        # stack.append(root)
        # while len(stack):
        #     cur_node = stack.pop()
        #     ans.append(cur_node.val)
        #     if cur_node.left: stack.append(cur_node.left)
        #     if cur_node.right: stack.append(cur_node.right)
        # # ans.reverse()
        # # return ans
        # return list(reversed(ans))

        # 统一风格迭代法
        '''
        71/71 cases passed (30 ms)
        Your runtime beats 94.34 % of python3 submissions
        Your memory usage beats 64.74 % of python3 submissions (16.4 MB)
        '''
        ans = []
        if not root: return ans
        stack = []
        stack.append(root)
        while stack:
            cur_node = stack.pop()
            if cur_node:
                stack.append(cur_node)
                stack.append(None)
                if cur_node.right: stack.append(cur_node.right)
                if cur_node.left: stack.append(cur_node.left)
            else:
                cur_node = stack.pop()
                ans.append(cur_node.val)

        return ans


# @lc code=end
