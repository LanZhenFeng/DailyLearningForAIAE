#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 递归+层次遍历
        '''
        38/38 cases passed (46 ms)
        Your runtime beats 81.13 % of python3 submissions
        Your memory usage beats 69.71 % of python3 submissions (18 MB)
        '''
        # ans = []

        # def order(node: 'Node', ans: List[List[int]], depth: int = 0):
        #     if node is None:
        #         return None
        #     if len(ans) == depth:
        #         ans.append([])
        #     ans[depth].append(node.val)
        #     for child in node.children:
        #         order(child, ans, depth + 1)

        # order(root, ans)
        # return ans

        # 迭代+层次遍历
        '''
        38/38 cases passed (41 ms)
        Your runtime beats 95.84 % of python3 submissions
        Your memory usage beats 50.84 % of python3 submissions (18 MB)
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
                for child in node.children:
                    if child: queue.append(child)
            ans.append(sub_ans)
        return ans


# @lc code=end
