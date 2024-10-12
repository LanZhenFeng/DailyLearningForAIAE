#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 借助栈和辅助数组
        '''
        35/35 cases passed (34 ms)
        Your runtime beats 90.38 % of python3 submissions
        Your memory usage beats 36.58 % of python3 submissions (17.1 MB)
        '''
        # ans = []
        # if not root: return ans
        # stack = []
        # stack.append(root)
        # cur_node = None
        # while stack:
        #     sub_ans = []
        #     temp = []
        #     while stack:
        #         cur_node = stack.pop()
        #         sub_ans.append(cur_node.val)
        #         if cur_node.left: temp.append(cur_node.left)
        #         if cur_node.right: temp.append(cur_node.right)
        #     stack.extend(temp[::-1])
        #     ans.append(sub_ans)
        # return ans

        # 借助队列和辅助数组
        '''
        35/35 cases passed (31 ms)
        Your runtime beats 96.64 % of python3 submissions
        Your memory usage beats 85.82 % of python3 submissions (16.9 MB)
        '''
        # ans = []
        # from collections import deque
        # if not root: return ans
        # queue = deque()
        # queue.append(root)
        # while queue:
        #     size = len(queue)
        #     sub_ans = []
        #     for i in range(size):
        #         node = queue.popleft()
        #         sub_ans.append(node.val)
        #         if node.left: queue.append(node.left)
        #         if node.right: queue.append(node.right)
        #     ans.append(sub_ans)
        # return ans

        # 递归法
        '''
        35/35 cases passed (23 ms)
        Your runtime beats 99.89 % of python3 submissions
        Your memory usage beats 5 % of python3 submissions (17.5 MB)
        '''
        ans = []

        def order(root, ans, depth):
            if not root: return
            if len(ans) == depth:
                ans.append([])
            ans[depth].append(root.val)
            if root.left: order(root.left, ans, depth + 1)
            if root.right: order(root.right, ans, depth + 1)

        order(root, ans, 0)
        return ans


# @lc code=end
