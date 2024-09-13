#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
from typing import List
# @lc code=start
class Solution:

    # def BinarySearch(target, nums):

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 方法一：取巧的暴力解法，控制台取巧勉强能过 🤣
        # max_value = max(nums)
        # if max_value >= target:
        #     return 1
        # ratio = target / (sum(nums))
        # start = int(len(nums)*ratio) -50 if int(len(nums)*ratio) -50 >1 else 1
        # for l in range(start, len(nums)):
        #     cumsum=0+sum(nums[0:l+1])
        #     if cumsum>=target:
        #         return l+1
        #     for i in range(len(nums)-l-1):
        #         if nums[i+l+1]-nums[i]+cumsum >=target:
        #             return l+1
        #         cumsum+=nums[i+l+1]-nums[i]
        # return 0

        # 方法二： 前缀和 + 二分查找，勉强能过
        # if not nums:
        #     return 0
        # if sum(nums) < target:
        #     return 0
        # if sum(nums) == target:
        #     return len(nums)
        # cumsum = 0
        # # for i in range(len(nums)):
        # #     if i == 0:
        # #         cumsum = nums[i]
        # #         nums[i] = 0
        # #     else:
        # #         temp = nums[i]
        # #         nums[i] = cumsum
        # #         cumsum = cumsum + temp
        # # nums.append(cumsum)

        # res = [0]
        # for i in range(len(nums)):
        #     res.append(nums[i] + cumsum)
        #     cumsum += nums[i]
        # ans = len(res)
        # import bisect
        # for i in range(len(res)):
        #     index = bisect.bisect_left(res, res[i]+target)
        #     if index != len(res):
        #         ans = min(ans, index - i)
        # return 0 if ans == len(res) else ans
        
        # 方法三： 滑动窗口
        ans = len(nums) + 1
        p1 = 0
        p2 = 0 
        # 利用sum()在判例18会超时
        # while p2 < len(nums):
        #     while p2 < len(nums) and sum(nums[p1:p2+1]) < target:
        #         p2 += 1
        #     while p1 < p2 and sum(nums[p1+1:p2+1]) >= target:
        #         p1 += 1
        #     if sum(nums[p1:p2+1]) >= target:
        #         ans = min(ans, p2-p1+1)
        #     p2 += 1
        cur_sum = 0
        while p2 < len(nums):
            while cur_sum < target and p2 < len(nums):
                cur_sum += nums[p2]
                p2 += 1
            
            while cur_sum >= target:
                ans = min(ans, p2-p1)
                cur_sum -= nums[p1]
                p1 += 1
            
        return 0 if ans == len(nums) + 1 else ans
    

# @lc code=end

