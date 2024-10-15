#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 中序->数组 再计算
        '''
        189/189 cases passed (42 ms)
        Your runtime beats 92.95 % of python3 submissions
        Your memory usage beats 6.92 % of python3 submissions (18.6 MB)
        '''
        # arr = []

        # def traversal(node, arr):
        #     if not node: return None

        #     traversal(node.left, arr)
        #     arr.append(node.val)
        #     traversal(node.right, arr)

        # traversal(root, arr)
        # import sys
        # minimumDifference = sys.maxsize
        # for i in range(1, len(arr)):
        #     if arr[i] - arr[i - 1] < minimumDifference:
        #         minimumDifference = arr[i] - arr[i - 1]
        # return minimumDifference

        # 遍历
        '''
        189/189 cases passed (42 ms)
        Your runtime beats 92.95 % of python3 submissions
        Your memory usage beats 70.43 % of python3 submissions (18.4 MB)
        '''
        import sys
        minimumDifference = sys.maxsize
        pre_node = None

        def traversal(node):
            if not node: return None

            traversal(node.left)
            nonlocal pre_node
            if pre_node:
                nonlocal minimumDifference
                minimumDifference = min(minimumDifference,
                                        node.val - pre_node.val)
            pre_node = node
            traversal(node.right)

        traversal(root)
        return minimumDifference

        # 迭代
        '''
        189/189 cases passed (46 ms)
        Your runtime beats 81.26 % of python3 submissions
        Your memory usage beats 58.04 % of python3 submissions (18.4 MB)
        '''
        import sys
        minimumDifference = sys.maxsize
        stack = []
        cur_node = root
        pre_node = None
        while cur_node or len(stack):
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()
                if pre_node:
                    minimumDifference = min(minimumDifference,
                                            cur_node.val - pre_node.val)
                pre_node = cur_node
                cur_node = cur_node.right
        return minimumDifference


# @lc code=end
