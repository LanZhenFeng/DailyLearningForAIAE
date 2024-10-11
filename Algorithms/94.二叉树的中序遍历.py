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
        # ans = []

        # def traversal(root, ans):
        #     if root is None:
        #         return

        #     traversal(root.left, ans)
        #     ans.append(root.val)
        #     traversal(root.right, ans)

        # traversal(root, ans)
        # return ans

        # 迭代法
        '''
        71/71 cases passed (32 ms)
        Your runtime beats 89.7 % of python3 submissions
        Your memory usage beats 86.64 % of python3 submissions (16.3 MB)
        '''
        # ans = []
        # if not root:
        #     return ans
        # # stack = [root]
        # cur_node = root
        # # while len(stack):
        # #     if cur_node:
        # #         stack.append(cur_node)
        # #         cur_node = cur_node.left
        # #     else:
        # #         cur_node = stack.pop()
        # #         ans.append(cur_node.val)
        # #         cur_node = cur_node.right
        # # return ans[:-1]
        # stack = []
        # while cur_node or len(stack):
        #     if cur_node:
        #         stack.append(cur_node)
        #         cur_node = cur_node.left
        #     else:
        #         cur_node = stack.pop()
        #         ans.append(cur_node.val)
        #         cur_node = cur_node.right
        # return ans

        # 统一风格迭代法
        '''
        71/71 cases passed (32 ms)
        Your runtime beats 89.7 % of python3 submissions
        Your memory usage beats 8.87 % of python3 submissions (16.5 MB)
        '''
        ans = []
        if not root: return ans
        stack = []
        stack.append(root)
        while stack:
            cur_node = stack.pop()
            if cur_node:
                if cur_node.right: stack.append(cur_node.right)
                stack.append(cur_node)
                stack.append(None)
                if cur_node.left: stack.append(cur_node.left)
            else:
                cur_node = stack.pop()
                ans.append(cur_node.val)

        return ans


# @lc code=end
