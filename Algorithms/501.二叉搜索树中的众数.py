#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # 中序遍历+记录各元素出现频率
        '''
        24/24 cases passed (42 ms)
        Your runtime beats 90.86 % of python3 submissions
        Your memory usage beats 5.21 % of python3 submissions (20.4 MB)
        '''
        # modes = {}

        # def traversal(node, modes):
        #     if not node: return None
        #     traversal(node.left, modes)
        #     modes[node.val] = modes.get(node.val, 0) + 1
        #     traversal(node.right, modes)

        # traversal(root, modes)
        # modes_list = sorted(modes.items(),
        #                     key=lambda item: item[1],
        #                     reverse=True)
        # ans = [modes_list[0][0]]
        # for i in range(1, len(modes_list)):
        #     if modes_list[i][1] == modes_list[0][1]:
        #         ans.append(modes_list[i][0])
        #     else:
        #         break
        # return ans

        # 递归+中序遍历+直接处理
        '''
        24/24 cases passed (36 ms)
        Your runtime beats 98.76 % of python3 submissions
        Your memory usage beats 40.71 % of python3 submissions (20 MB)
        '''
        # modes = []
        # pre_val = None
        # max_freq = 0
        # cur_freq = 0

        # def traversal(node, modes):
        #     if not node: return None
        #     traversal(node.left, modes)

        #     nonlocal pre_val, cur_freq, max_freq
        #     if pre_val is None:
        #         cur_freq = 1
        #     else:
        #         if node.val == pre_val:
        #             cur_freq += 1
        #         else:
        #             cur_freq = 1
        #     pre_val = node.val

        #     if cur_freq == max_freq:
        #         modes.append(pre_val)
        #     elif cur_freq > max_freq:
        #         max_freq = cur_freq
        #         modes.clear()
        #         modes.append(pre_val)
        #     traversal(node.right, modes)

        # traversal(root, modes)
        # return modes

        # 迭代+中序遍历+直接处理
        '''
        24/24 cases passed (43 ms)
        Your runtime beats 87.98 % of python3 submissions
        Your memory usage beats 32.87 % of python3 submissions (20.1 MB)
        '''
        modes = []
        max_freq = 0
        cur_freq = 0
        stack = []
        cur_node = root
        pre_node = None
        while cur_node or stack:

            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()
                if not pre_node:
                    cur_freq = 1
                elif cur_node.val == pre_node.val:
                    cur_freq += 1
                else:
                    cur_freq = 1
                pre_node = cur_node
                if cur_freq == max_freq:
                    modes.append(cur_node.val)
                elif cur_freq > max_freq:
                    max_freq = cur_freq
                    modes.clear()
                    modes.append(cur_node.val)
                cur_node = cur_node.right

        return modes


# @lc code=end
