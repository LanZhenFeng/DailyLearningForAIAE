#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 方法一：双指针
        ans = []
        nums.sort()
        for i in range(len(nums)-3):
            if nums[i] > target and (target >= 0 or nums[i] >= 0): break
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]: continue
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s < target:
                        k += 1
                        while k < l and nums[k] == nums[k-1]: 
                            k += 1
                    elif s > target:
                        l -= 1
                        while k < l and nums[l] == nums[l+1]: 
                            l -= 1
                    else:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]: k += 1
                        while k < l and nums[l] == nums[l+1]: l -= 1
        return ans
# @lc code=end

