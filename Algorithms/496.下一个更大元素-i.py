#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#


# @lc code=start
class Solution:

    def nextGreaterElement(self, nums1: List[int],
                           nums2: List[int]) -> List[int]:
        # 单调栈
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        '''
        16/16 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 57.51 % of python3 submissions (16.6 MB)
        '''
        res = [-1] * len(nums1)
        umap = {}
        for i in range(len(nums1)):
            umap[nums1[i]] = i
        stack = [nums2[0]]
        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                if stack[-1] in umap:
                    res[umap[stack[-1]]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        return res


# @lc code=end
