#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 递归+层次遍历 + 取最后一个值
        '''
        216/216 cases passed (29 ms)
        Your runtime beats 96.73 % of python3 submissions
        Your memory usage beats 5.05 % of python3 submissions (16.6 MB)
        '''
        # ans = []

        # def order(node: Optional[TreeNode],
        #           ans: List[List[int]],
        #           depth: int = 0):
        #     if node is None:
        #         return None
        #     if len(ans) == depth:
        #         ans.append([])
        #     ans[depth].append(node.val)
        #     order(node.left, ans, depth + 1)
        #     order(node.right, ans, depth + 1)

        # order(root, ans)
        # return [row[-1] for row in ans]

        # 迭代+层次遍历 + 取最后一个值
        '''
        216/216 cases passed (30 ms)
        Your runtime beats 95.07 % of python3 submissions
        Your memory usage beats 5.05 % of python3 submissions (16.6 MB)
        '''
        ans = []
        from collections import deque
        if not root: return ans
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == size - 1:
                    ans.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return ans


# @lc code=end
