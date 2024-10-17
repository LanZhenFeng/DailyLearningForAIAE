#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def deleteNode(self, root: Optional[TreeNode],
                   key: int) -> Optional[TreeNode]:

        # 递归
        '''
        92/92 cases passed (48 ms)
        Your runtime beats 77.76 % of python3 submissions
        Your memory usage beats 10.86 % of python3 submissions (20.2 MB)
        '''

        def traversal(root, key):
            if not root: return None
            if key < root.val:
                root.left = traversal(root.left, key)
            elif key > root.val:
                root.right = traversal(root.right, key)
            else:
                if not root.left and not root.right:
                    return None
                elif not root.left and root.right:
                    return root.right
                elif root.left and not root.right:
                    return root.left
                else:
                    ptr = root.right
                    while ptr.left:
                        ptr = ptr.left
                    ptr.left = root.left
                    return root.right
            return root

        return traversal(root, key)

        # TODO 迭代法 稍微复杂些

        # 思路错误
        '''
        48/92 cases passed (N/A)
        '''
        # if not root: return None
        # if not root.left and not root.right and key == root.val: return None
        # pre_node = root
        # ptr = root
        # while ptr:
        #     if key < ptr.val:
        #         pre_node = ptr
        #         ptr = ptr.left
        #     elif key > ptr.val:
        #         pre_node = ptr
        #         ptr = ptr.right
        #     else:
        #         if not ptr.left and not ptr.right:
        #             pre_node.left = None
        #             pre_node.right = None
        #         elif not ptr.left and ptr.right:
        #             pre_node.left = ptr.right
        #         elif not ptr.right and ptr.left:
        #             pre_node.right = ptr.left
        #         else:
        #             ptr.right.left = ptr.left
        #             if ptr is root:
        #                 root = root.right
        #             else:
        #                 pre_node.left = ptr.right
        #         break

        # return root


# @lc code=end
