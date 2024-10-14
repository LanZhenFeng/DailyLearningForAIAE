#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 递归
        '''
        208/208 cases passed (31 ms)
        Your runtime beats 93.72 % of python3 submissions
        Your memory usage beats 17.9 % of python3 submissions (16.5 MB)
        '''
        # ans = []
        # res = ""

        # def getPaths(node, res):
        #     if not res:
        #         # res = str(node.val)
        #         res = ''.join([res, str(node.val)])
        #     else:
        #         # res = res + '->' + str(node.val)
        #         res = '->'.join([res, str(node.val)])
        #     if not node.left and not node.right:
        #         nonlocal ans
        #         ans.append(res)
        #     if node.left: getPaths(node.left, res)
        #     if node.right: getPaths(node.right, res)

        # getPaths(root, res)

        # return ans

        # 递归+回溯
        '''
        208/208 cases passed (26 ms)
        Your runtime beats 98.6 % of python3 submissions
        Your memory usage beats 5.32 % of python3 submissions (16.6 MB)
        '''
        # ans = []
        # path = []

        # def getPaths(node, path: List):
        #     path.append(node.val)
        #     if not node.left and not node.right:
        #         nonlocal ans
        #         ans.append('->'.join(list(map(str, path))))
        #     if node.left:
        #         getPaths(node.left, path)
        #         path.pop()
        #     if node.right:
        #         getPaths(node.right, path)
        #         path.pop()

        # getPaths(root, path)

        # return ans

        # 迭代
        '''
        208/208 cases passed (30 ms)
        Your runtime beats 95.24 % of python3 submissions
        Your memory usage beats 26 % of python3 submissions (16.5 MB)
        '''
        ans = []
        path = []

        stack = [root]
        path.append([root.val])
        while stack:
            cur_node = stack.pop()
            cur_path = path.pop()
            if not cur_node.left and not cur_node.right:
                pathSt = "->".join(list(map(str, cur_path)))
                ans.append(pathSt)
            if cur_node.right:
                stack.append(cur_node.right)
                new_cur_path = cur_path.copy()
                new_cur_path.append(cur_node.right.val)
                path.append(new_cur_path)
            if cur_node.left:
                stack.append(cur_node.left)
                new_cur_path = cur_path.copy()
                new_cur_path.append(cur_node.left.val)
                path.append(new_cur_path)

        return ans


# @lc code=end
