#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 迭代+栈+前序遍历 O(n)
        '''
        18/18 cases passed (56 ms)
        Your runtime beats 73.39 % of python3 submissions
        Your memory usage beats 43.48 % of python3 submissions (22 MB)
        '''

        # ans = 0
        # if not root: return ans
        # stack = [root]
        # while stack:
        #     cur_node = stack.pop()
        #     if cur_node:
        #         if cur_node.right: stack.append(cur_node.right)
        #         if cur_node.left: stack.append(cur_node.left)
        #         stack.append(cur_node)
        #         stack.append(None)
        #     else:
        #         cur_node = stack.pop()
        #         ans += 1

        # return ans

        # 迭代+队列+层次遍历 O(n)
        '''
        18/18 cases passed (43 ms)
        Your runtime beats 98.99 % of python3 submissions
        Your memory usage beats 8.88 % of python3 submissions (22.1 MB)
        '''

        # ans = 0
        # if not root: return ans
        # from collections import deque
        # queue = deque([root])
        # while queue:
        #     cur_node = queue.popleft()
        #     ans += 1
        #     if cur_node.right: queue.append(cur_node.right)
        #     if cur_node.left: queue.append(cur_node.left)

        # return ans

        # 递归+层次遍历 O(n)
        '''
        18/18 cases passed (56 ms)
        Your runtime beats 73.39 % of python3 submissions
        Your memory usage beats 65.67 % of python3 submissions (22 MB)
        '''

        # def getNodeNums(node):
        #     if not node:
        #         return 0

        #     leftNodeNums = getNodeNums(node.left)
        #     rightNodeNums = getNodeNums(node.right)

        #     return 1 + leftNodeNums + rightNodeNums

        # ans = getNodeNums(root)
        # return ans

        # 完全二叉树
        '''
        18/18 cases passed (43 ms)
        Your runtime beats 98.99 % of python3 submissions
        Your memory usage beats 28.85 % of python3 submissions (22 MB)
        '''

        # def getNodeNums(node):
        #     if not node: return 0
        #     leftdepth = 1
        #     rightdepth = 1
        #     leftNode = node.left
        #     while leftNode:
        #         leftdepth += 1
        #         leftNode = leftNode.left
        #     rightNode = node.right
        #     while rightNode:
        #         rightdepth += 1
        #         rightNode = rightNode.right
        #     if leftdepth == rightdepth:
        #         return 2**leftdepth - 1
        #     else:
        #         return getNodeNums(node.left) + getNodeNums(node.right) + 1

        # ans = getNodeNums(root)
        # return ans

        # 完全二叉树 写法2
        '''
        18/18 cases passed (47 ms)
        Your runtime beats 96.13 % of python3 submissions
        Your memory usage beats 28.85 % of python3 submissions (22 MB)
        '''

        def getNodeNums(node):
            if not node: return 0
            depth = 0
            leftNode = node.left
            rightNode = node.right

            while leftNode and rightNode:
                depth += 1
                leftNode = leftNode.left
                rightNode = rightNode.right
            if not leftNode and not rightNode:
                return (2 << depth) - 1
            else:
                return getNodeNums(node.left) + getNodeNums(node.right) + 1

        ans = getNodeNums(root)
        return ans


# @lc code=end
