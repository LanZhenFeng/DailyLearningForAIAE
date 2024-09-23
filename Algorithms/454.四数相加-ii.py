#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 方法一：暴力求解 
        # !!!超时!!!
        # ans = 0
        # for n1 in nums1:
        #     for n2 in nums2:
        #         for n3 in nums3:
        #             for n4 in nums4:
        #                 if n1+n2+n3+n4==0:
        #                     ans += 1
        # return ans
        
        # 方法二：将第四个列表转化为字典（哈希表）
        # !!! 还是超时 !!!
        # ans = 0
        # nums4_dic = dict()
        # for i in range(len(nums4)):
        #     nums4_dic[nums4[i]] = nums4_dic.get(nums4[i], 0) + 1
        
        # for n1 in nums1:
        #     for n2 in nums2:
        #         for n3 in nums3:
        #             if -n1-n2-n3 in nums4_dic.keys():
        #                 ans+=nums4_dic.get(-n1-n2-n3, 0)
        # return ans

        # 方法三：全字典+分治
        '''
        132/132 cases passed (285 ms)
        Your runtime beats 99.62 % of python3 submissions
        Your memory usage beats 7.54 % of python3 submissions (16.8 MB)
        '''
        ans = 0
        nums1_dic = defaultdict(int)
        nums2_dic = defaultdict(int)
        nums3_dic = defaultdict(int)
        nums4_dic = defaultdict(int)
        for n1 in nums1:
            nums1_dic[n1] += 1
        for n2 in nums2:
            nums2_dic[n2] += 1
        for n3 in nums3:
            nums3_dic[n3] += 1
        for n4 in nums4:
            nums4_dic[n4] += 1

        dic12 = defaultdict(int)
        for k1 in nums1_dic:
            for k2 in nums2_dic:
                dic12[k1+k2] += nums1_dic[k1] * nums2_dic[k2]
        
        dic34 = defaultdict(int)
        for k3 in nums3_dic:
            for k4 in nums4_dic:
                dic34[k3+k4] += nums3_dic[k3] * nums4_dic[k4]
        
        for k12 in dic12:
            if -k12 in dic34:
                ans+=dic12[k12]*dic34[-k12]

        return ans
    

# @lc code=end

