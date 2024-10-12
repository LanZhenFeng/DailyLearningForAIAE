#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # 递归+层次遍历 + 取平均值
        '''
        66/66 cases passed (38 ms)
        Your runtime beats 95.75 % of python3 submissions
        Your memory usage beats 85.35 % of python3 submissions (18.6 MB)
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
        # avg_ans = []
        # for sub_ans in ans:
        #     avg_ans.append(sum(sub_ans) / len(sub_ans))
        # return avg_ans

        # 迭代+层次遍历 + 取平均值
        '''
        66/66 cases passed (34 ms)
        Your runtime beats 98.79 % of python3 submissions
        Your memory usage beats 17.79 % of python3 submissions (18.7 MB)
        '''
        ans = []
        from collections import deque
        if not root: return ans
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            sub_ans = []
            for i in range(size):
                node = queue.popleft()
                sub_ans.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(sum(sub_ans) / len(sub_ans))
        return ans


# @lc code=end
