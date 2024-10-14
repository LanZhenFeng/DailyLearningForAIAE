#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, right=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 递归
        '''
        117/117 cases passed (31 ms)
        Your runtime beats 98.95 % of python3 submissions
        Your memory usage beats 32.08 % of python3 submissions (17.5 MB)
        '''
        # if not root: return False

        # def traversal(node, cur_value, targetSum):
        #     # print(node.val, cur_value)
        #     if not (node.left or node.right) and cur_value == targetSum:
        #         return True
        #     if not (node.left or node.right): return False

        #     if node.left:
        #         cur_value += node.left.val
        #         if traversal(node.left, cur_value, targetSum): return True
        #         cur_value -= node.left.val
        #     if node.right:
        #         cur_value += node.right.val
        #         if traversal(node.right, cur_value, targetSum): return True
        #         cur_value -= node.right.val

        #     return False

        # return traversal(root, root.val, targetSum)

        # 迭代
        '''
        117/117 cases passed (31 ms)
        Your runtime beats 98.95 % of python3 submissions
        Your memory usage beats 20.01 % of python3 submissions (17.6 MB)
        '''
        if not root: return False

        stack = [root]
        sum_list = [root.val]
        while stack:
            cur_node = stack.pop()
            cur_sum = sum_list.pop()
            if not cur_node.left and not cur_node.right and cur_sum == targetSum:
                return True
            if cur_node.right:
                stack.append(cur_node.right)
                sum_list.append(cur_sum + cur_node.right.val)
            if cur_node.left:
                stack.append(cur_node.left)
                sum_list.append(cur_sum + cur_node.left.val)

        return False


# @lc code=end
