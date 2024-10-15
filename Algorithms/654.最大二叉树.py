#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def constructMaximumBinaryTree(self,
                                   nums: List[int]) -> Optional[TreeNode]:

        # 递归 [ )
        '''
        107/107 cases passed (73 ms)
        Your runtime beats 92.78 % of python3 submissions
        Your memory usage beats 13.45 % of python3 submissions (17 MB)
        '''

        # def traversal(nums, begin, end):
        #     if begin == end: return None
        #     delimiterIndex = begin
        #     for i in range(begin + 1, end):
        #         if nums[i] > nums[delimiterIndex]:
        #             delimiterIndex = i
        #     max_val = nums[delimiterIndex]
        #     root = TreeNode(max_val)
        #     if end - begin == 1: return root

        #     root.left = traversal(nums, begin, delimiterIndex)

        #     root.right = traversal(nums, delimiterIndex + 1, end)
        #     return root

        # return traversal(nums, 0, len(nums))

        # 递归：切片
        '''
        107/107 cases passed (78 ms)
        Your runtime beats 82.65 % of python3 submissions
        Your memory usage beats 82.55 % of python3 submissions (16.8 MB)
        '''
        if not nums: return None
        max_val = max(nums)
        root = TreeNode(max_val)
        delimiterIndex = nums.index(max_val)
        root.left = self.constructMaximumBinaryTree(nums[:delimiterIndex])
        root.right = self.constructMaximumBinaryTree(nums[delimiterIndex + 1:])
        return root


# @lc code=end
