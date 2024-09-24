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
                    
# @lc code=end

