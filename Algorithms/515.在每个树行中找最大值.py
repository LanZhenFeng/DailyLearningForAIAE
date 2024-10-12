#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # 递归+层次遍历+取最大值
        '''
        78/78 cases passed (34 ms)
        Your runtime beats 97.16 % of python3 submissions
        Your memory usage beats 24.25 % of python3 submissions (18.7 MB)
        '''
        ans = []

        def order(node: Optional[TreeNode],
                  ans: List[List[int]],
                  depth: int = 0):
            if node is None:
                return None
            if len(ans) == depth:
                ans.append([])
            ans[depth].append(node.val)
            order(node.left, ans, depth + 1)
            order(node.right, ans, depth + 1)

        order(root, ans)
        max_ans = []
        for sub_ans in ans:
            max_ans.append(max(sub_ans))
        return max_ans

        # 迭代+层次遍历+取最大值
        '''
        78/78 cases passed (37 ms)
        Your runtime beats 92.59 % of python3 submissions
        Your memory usage beats 7.03 % of python3 submissions (18.7 MB)
        '''
        ans = []
        import sys
        from collections import deque
        if not root: return ans
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            max_val = -sys.maxsize
            for i in range(size):
                node = queue.popleft()
                if node.val > max:
                    max_val = node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(max)
        return ans


# @lc code=end
