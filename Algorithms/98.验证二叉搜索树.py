#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 递归
        '''
        85/85 cases passed (28 ms)
        Your runtime beats 99.78 % of python3 submissions
        Your memory usage beats 92.39 % of python3 submissions (18.3 MB)
        '''
        # self.max_val = -(2**31) - 1

        # def isValid(root):
        #     if not root: return True
        #     left = isValid(root.left)
        #     if self.max_val < root.val: self.max_val = root.val
        #     else: return False
        #     right = isValid(root.right)
        #     return left and right

        # return isValid(root)

        # 中序遍历+数组递增判断
        '''
        85/85 cases passed (38 ms)
        Your runtime beats 89.85 % of python3 submissions
        Your memory usage beats 69.02 % of python3 submissions (18.4 MB)
        '''
        # arr = []

        # def traversal(node, arr):
        #     if not node: return None
        #     traversal(node.left, arr)
        #     arr.append(node.val)
        #     traversal(node.right, arr)

        # traversal(root, arr)
        # for i in range(1, len(arr)):
        #     if arr[i] <= arr[i - 1]:
        #         return False
        # return True

        # 迭代
        '''
        85/85 cases passed (35 ms)
        Your runtime beats 95.92 % of python3 submissions
        Your memory usage beats 5.18 % of python3 submissions (18.7 MB)
        '''
        stack = []
        cur_node = root
        pre_node = None
        while cur_node or len(stack):
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()
                if pre_node and cur_node.val <= pre_node.val:
                    return False
                pre_node = cur_node
                cur_node = cur_node.right
        return True


# @lc code=end
