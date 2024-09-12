#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        方法一：
        '''
        offset = 0   
        lens = len(nums)
        i = 0
        # range得到的可迭代对象只能往前，无法执行i=i-1
        while i < lens:
            if i+offset >= lens:
                break
            if val == nums[i]:
                nums.pop(i)
                i = i-1
                offset += 1
            i = i+1
        return len(nums)
        # '''
        # 方法二：
        # '''
        # k = 0
        # f = 0
        # offset = 0
        # last_index = len(nums)
        # for i in range(last_index):
        #     if nums[(i+offset)%last_index] == val:
        #         while i+offset <= last_index - 1:
        #             k += 1
        #             offset += 1
        #             if nums[(i+offset)%last_index] != val:
        #                 break
        #     nums[i] = nums[(i+offset)%last_index]
        # return last_index - k

# @lc code=end

