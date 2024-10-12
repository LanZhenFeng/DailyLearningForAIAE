#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 迭代+自顶向下的层序遍历+逆序
        '''
        34/34 cases passed (35 ms)
        Your runtime beats 82.11 % of python3 submissions
        Your memory usage beats 11.59 % of python3 submissions (16.8 MB)
        '''
        # ans = []
        # if not root: return ans
        # from collections import deque
        # queue = deque()
        # queue.append(root)
        # while queue:
        #     sub_ans = []
        #     size = len(queue)
        #     for _ in range(size):
        #         node = queue.popleft()
        #         sub_ans.append(node.val)
        #         if node.left: queue.append(node.left)
        #         if node.right: queue.append(node.right)
        #     ans.append(sub_ans)
        # return ans[::-1]

        # 递归+自顶向下的层序遍历+逆序
        '''
        34/34 cases passed (29 ms)
        Your runtime beats 96.68 % of python3 submissions
        Your memory usage beats 9.8 % of python3 submissions (16.8 MB)
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
        # return ans[::-1]

        # 递归+自底向上的层序遍历
        '''
        34/34 cases passed (23 ms)
        Your runtime beats 99.74 % of python3 submissions
        Your memory usage beats 47.15 % of python3 submissions (16.7 MB)
        '''
        # ans = []

        # def order(node: Optional[TreeNode],
        #           ans: List[List[int]],
        #           depth: int = 0):
        #     if node is None:
        #         return None
        #     if len(ans) == depth:
        #         ans.insert(0, [])
        #     order(node.left, ans, depth + 1)
        #     order(node.right, ans, depth + 1)
        #     ans[-(depth + 1)].append(node.val)

        # order(root, ans)
        # return ans

        # 递归+自底向上的层序遍历
        '''
        34/34 cases passed (30 ms)
        Your runtime beats 95.42 % of python3 submissions
        Your memory usage beats 5.03 % of python3 submissions (16.9 MB)
        '''
        ans = []
        if not root: return ans
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            sub_ans = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                sub_ans.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.insert(0, sub_ans)
        return ans


# @lc code=end
