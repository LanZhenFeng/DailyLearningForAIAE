#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
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

    def preorder(self, root: 'Node') -> List[int]:
        # 递归法
        '''
        39/39 cases passed (30 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 5.45 % of python3 submissions (18.1 MB)
        '''
        # ans = []

        # def traversal(node, ans):
        #     if node is None:
        #         return

        #     ans.append(node.val)
        #     for child in node.children:
        #         if child: traversal(child, ans)

        # traversal(root, ans)
        # return ans

        # 迭代法
        '''
        39/39 cases passed (41 ms)
        Your runtime beats 93.4 % of python3 submissions
        Your memory usage beats 70.01 % of python3 submissions (18 MB)
        '''
        # ans = []
        # if not root:
        #     return ans
        # stack = []
        # stack.append(root)
        # while len(stack):
        #     cur_node = stack.pop()
        #     ans.append(cur_node.val)
        #     for child in cur_node.children[::-1]:
        #         if child: stack.append(child)
        # return ans

        # 统一风格迭代法
        '''
        39/39 cases passed (38 ms)
        Your runtime beats 97.42 % of python3 submissions
        Your memory usage beats 87.66 % of python3 submissions (17.9 MB)
        '''
        ans = []
        if not root: return ans
        stack = []
        stack.append(root)
        while stack:
            cur_node = stack.pop()
            if cur_node:
                for child in cur_node.children[::-1]:
                    if child: stack.append(child)
                stack.append(cur_node)
                stack.append(None)
            else:
                cur_node = stack.pop()
                ans.append(cur_node.val)

        return ans


# @lc code=end
