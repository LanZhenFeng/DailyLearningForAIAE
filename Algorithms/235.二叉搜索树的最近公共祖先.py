#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        # 递归 二叉树
        '''
        30/30 cases passed (44 ms)
        Your runtime beats 99.21 % of python3 submissions
        Your memory usage beats 63.82 % of python3 submissions (20 MB)
        '''

        # if root is p or root is q or root is None: return root
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)
        # if left and right:
        #     return root
        # if not left:
        #     return right
        # return left

        # 递归 二叉搜索树
        '''
        30/30 cases passed (43 ms)
        Your runtime beats 99.62 % of python3 submissions
        Your memory usage beats 5.14 % of python3 submissions (20.2 MB)
        '''

        # if not root: return None
        # p_val = p.val
        # q_val = q.val
        # min_val = min(p_val, q_val)
        # max_val = max(p_val, q_val)
        # if min_val <= root.val <= max_val: return root
        # left = self.lowestCommonAncestor(root.left, p, q)
        # if left: return left
        # right = self.lowestCommonAncestor(root.right, p, q)
        # if right: return right

        # 递归 二叉搜索树 写法2
        '''
        30/30 cases passed (54 ms)
        Your runtime beats 86.62 % of python3 submissions
        Your memory usage beats 44.48 % of python3 submissions (20 MB)
        '''

        # if not root: return root
        # if root.val > p.val and root.val > q.val:
        #     left = self.lowestCommonAncestor(root.left, p, q)
        #     if left: return left
        # elif root.val < p.val and root.val < q.val:
        #     right = self.lowestCommonAncestor(root.right, p, q)
        #     if right: return right
        # else: return root

        # 迭代 二叉搜索树
        '''
        30/30 cases passed (52 ms)
        Your runtime beats 90.85 % of python3 submissions
        Your memory usage beats 5.14 % of python3 submissions (20.2 MB)
        '''
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
        return None


# @lc code=end
