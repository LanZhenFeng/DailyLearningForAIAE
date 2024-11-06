#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    memory = {}

    def rob(self, root: Optional[TreeNode]) -> int:
        # 递归 树遍历 暴力搜索
        # 时间复杂度：O(n^2)，这个时间复杂度不太标准，也不容易准确化，例如越往下的节点重复计算次数就越多
        # 空间复杂度：O(log n)，算上递推系统栈的空间
        '''
        Time Limit Exceeded
        122/124 cases passed (N/A)
        '''
        # if not root: return 0
        # if not root.left and not root.right: return root.val

        # rob_val = root.val
        # if root.left:
        #     rob_val += self.rob(root.left.left) + self.rob(root.left.right)
        # if root.right:
        #     rob_val += self.rob(root.right.left) + self.rob(root.right.right)

        # unrob_val = self.rob(root.left) + self.rob(root.right)

        # return max(rob_val, unrob_val)

        # 递归 树遍历 记忆化搜索
        # 时间复杂度：O(n)
        # 空间复杂度：O(log n)，算上递推系统栈的空间
        '''
        124/124 cases passed (3 ms)
        Your runtime beats 89.39 % of python3 submissions
        Your memory usage beats 15.92 % of python3 submissions (19.1 MB)
        '''

        # if not root: return 0
        # if not root.left and not root.right: return root.val

        # if self.memory.get(root): return self.memory[root]

        # rob_val = root.val
        # if root.left:
        #     rob_val += self.rob(root.left.left) + self.rob(root.left.right)
        # if root.right:
        #     rob_val += self.rob(root.right.left) + self.rob(root.right.right)

        # unrob_val = self.rob(root.left) + self.rob(root.right)

        # self.memory[root] = max(rob_val, unrob_val)

        # return max(rob_val, unrob_val)

        # 树形 DP
        # 时间复杂度：O(n)，每个节点只遍历了一次
        # 空间复杂度：O(log n)，算上递推系统栈的空间
        '''
        124/124 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 39.09 % of python3 submissions (18.4 MB)
        '''

        def traversal(node):
            if not node: return (0, 0)

            left = traversal(node.left)
            right = traversal(node.right)

            rob_val = node.val + left[0] + right[0]

            unrob_val = max(left) + max(right)

            return (unrob_val, rob_val)

        dp = traversal(root)
        return max(dp)


# @lc code=end
