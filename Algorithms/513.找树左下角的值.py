#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # 递归+层序遍历
        '''
        79/79 cases passed (39 ms)
        Your runtime beats 95.56 % of python3 submissions
        Your memory usage beats 5.04 % of python3 submissions (20.8 MB)
        '''
        # ans = []

        # def travel(node, depth):
        #     if len(ans) == depth:
        #         ans.append([])
        #     ans[depth].append(node.val)
        #     if node.left: travel(node.left, depth + 1)
        #     if node.right: travel(node.right, depth + 1)

        # travel(root, 0)
        # return ans[-1][0]

        # 递归+层序遍历 版本2
        '''
        79/79 cases passed (37 ms)
        Your runtime beats 97.66 % of python3 submissions
        Your memory usage beats 5.04 % of python3 submissions (20.1 MB)
        '''
        # ans = 0
        # maxDepth = -1

        # def traverval(node, depth):
        #     if not node.left and not node.right:
        #         nonlocal maxDepth
        #         if depth > maxDepth:
        #             maxDepth = depth
        #             nonlocal ans
        #             ans = node.val
        #     if node.left: traverval(node.left, depth + 1)
        #     if node.right: traverval(node.right, depth + 1)

        # traverval(root, 0)
        # return ans

        # 迭代+层序遍历
        '''
        79/79 cases passed (41 ms)
        Your runtime beats 91.59 % of python3 submissions
        Your memory usage beats 33.5 % of python3 submissions (19.1 MB)
        '''
        # ans = []
        # from collections import deque
        # queue = deque()
        # queue.append(root)
        # while queue:
        #     size = len(queue)
        #     sub_ans = []
        #     for i in range(size):
        #         cur_node = queue.popleft()
        #         sub_ans.append(cur_node.val)
        #         if cur_node.left: queue.append(cur_node.left)
        #         if cur_node.right: queue.append(cur_node.right)
        #     ans.append(sub_ans)

        # return ans[-1][0]

        # 迭代+层序遍历
        '''
        79/79 cases passed (43 ms)
        Your runtime beats 85.91 % of python3 submissions
        Your memory usage beats 69.27 % of python3 submissions (18.6 MB)
        '''
        ans = 0
        maxDepth = -1
        from collections import deque
        queue = deque()
        queue.append(root)
        depth = 0
        while queue:
            size = len(queue)
            depth += 1
            for i in range(size):
                cur_node = queue.popleft()
                if not cur_node.left and not cur_node.right:
                    if depth > maxDepth:
                        maxDepth = depth
                        ans = cur_node.val
                if cur_node.left: queue.append(cur_node.left)
                if cur_node.right: queue.append(cur_node.right)

        return ans


# @lc code=end
