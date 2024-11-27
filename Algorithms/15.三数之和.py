#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 想法错误，超时
        # ans = []
        # dict_23 = defaultdict(list)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         index_pair = sorted([i, j])
        #         if i != j and index_pair not in dict_23[nums[i]+nums[j]]:
        #             dict_23[nums[i]+nums[j]].append([i, j])
        # indices = []
        # for k in range(len(nums)):
        #     if -nums[k] in dict_23:
        #         for d_value in dict_23[-nums[k]]:
        #             if k not in d_value:
        #                 res = [k]
        #                 res.extend(d_value)
        #                 res.sort()
        #                 if res not in indices:
        #                     indices.append(res)
        # for i in indices:
        #     num = []
        #     for j in i:
        #         num.append(nums[j])
        #     num.sort()
        #     if num not in ans:
        #         ans.append(num)
        # return ans
        
        # 还是超时
        # ans = []
        # d1 = defaultdict(int)
        # for num in nums:
        #     d1[num] += 1

        # d23 = defaultdict(list)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         keys = sorted([i, j])
        #         d23[nums[i]+nums[j]].append(keys)
        
        # for k in range(len(nums)):
        #     if -nums[k] in d23.keys():
        #         for key_pair in d23[-nums[k]]:
        #             if k not in key_pair:
        #                 keys = sorted([nums[k], nums[key_pair[0]], nums[key_pair[1]]])
        #                 if keys not in ans:
        #                     ans.append(keys)
        
        # # d23 = defaultdict(list)
        # # for key1 in d1.keys():
        # #     for key2 in d1.keys():
        # #         keys = sorted([key1, key2])
        # #         if key1 != key2 and keys not in d23[key1+key2]:
        # #             d23[key1+key2].append(keys)
        # #         if key1 == key2 and d1[key1] >= 2 and keys not in d23[key1+key2]:
        # #             d23[key1+key2].append(keys)
        
        # # for key3 in d1.keys():
        # #     if -key3 in d23.keys():
        # #         for key_pair in d23[-key3]:
        # #             keys = sorted([key3, key_pair[0], key_pair[1]])
        # #             if keys not in ans and keys.count(key3) <= d1[key3]:
        # #                 ans.append(keys)
        # return ans

        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0: break # 1. because of j > i > k.
            if k > 0 and nums[k] == nums[k - 1]: continue # 2. skip the same `nums[k]`.
            i, j = k + 1, len(nums) - 1
            while i < j: # 3. double pointer
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res

        # 哈希表
        # 时间复杂度 O(n^2) ✅
        # 空间复杂度 O(n)，额外的 set 开销 ✅ 
        # ans = []
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         break
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     d = set()
        #     for j in range(i+1, len(nums)):
        #         if j > i+2 and nums[j] == nums[j-1] and nums[j-1] == nums[j-2]: continue
        #         c = 0 - nums[i] - nums[j]
        #         if c in d:
        #             ans.append([nums[i], nums[j], c])
        #             d.discard(c)
        #         else:
        #             d.add(nums[j])
        # return ans

        # 双指针
        # 时间复杂度 O(n^2) ✅
        # 空间复杂度 O(1)   ✅ 
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            x = nums[i]
            if x > 0:
                break
            if i > 0 and x == nums[i-1]:
                continue
            # if x + nums[i+1] + nums[i+2] > 0:
            #     break
            # if x + nums[-2] + nums[-1] < 0:
            #     continue
            left = i+1
            right = len(nums)-1
            while left < right:
                s = x + nums[left] + nums[right]
                if s == 0:
                    ans.append([x, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1
        return ans
                    
# @lc code=end

