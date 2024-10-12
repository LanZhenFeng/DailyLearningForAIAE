#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
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

    def postorder(self, root: 'Node') -> List[int]:
        # 递归法
        '''
        38/38 cases passed (41 ms)
        Your runtime beats 93.65 % of python3 submissions
        Your memory usage beats 51.68 % of python3 submissions (18 MB)
        '''
        # ans = []

        # def traversal(node, ans):
        #     if node is None:
        #         return

        #     for child in node.children:
        #         if child: traversal(child, ans)
        #     ans.append(node.val)

        # traversal(root, ans)
        # return ans

        # 迭代法
        '''
        38/38 cases passed (41 ms)
        Your runtime beats 93.65 % of python3 submissions
        Your memory usage beats 67.02 % of python3 submissions (18 MB)
        '''
        # ans = []
        # if not root:
        #     return ans
        # stack = []
        # stack.append(root)
        # while len(stack):
        #     cur_node = stack.pop()
        #     ans.append(cur_node.val)
        #     for child in cur_node.children:
        #         if child: stack.append(child)
        # return ans[::-1]

        # 统一风格迭代法
        '''
        38/38 cases passed (41 ms)
        Your runtime beats 93.65 % of python3 submissions
        Your memory usage beats 70.55 % of python3 submissions (18 MB)
        '''
        ans = []
        if not root: return ans
        stack = []
        stack.append(root)
        while stack:
            cur_node = stack.pop()
            if cur_node:
                stack.append(cur_node)
                stack.append(None)
                for child in cur_node.children[::-1]:
                    if child: stack.append(child)
            else:
                cur_node = stack.pop()
                ans.append(cur_node.val)

        return ans


# @lc code=end
