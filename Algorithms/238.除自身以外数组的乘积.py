#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#


# @lc code=start
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 暴力
        # 时间复杂度 O(n^2)
        # 空间复杂度 O(n)
        # answer = []
        # for i in range(len(nums)):
        #     cur_ans = 1
        #     for j in range(len(nums)):
        #         if j == i: continue
        #         cur_ans *= nums[j]
        #     answer.append(cur_ans)
        # return answer

        # 前后缀分解
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        # pre_products = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     pre_products[i] = pre_products[i-1] * nums[i-1]

        # suf_products = [1] * len(nums)
        # for i in range(len(nums)-2, -1, -1):
        #     suf_products[i] = suf_products[i+1] * nums[i+1]

        # return [p * s for p, s in zip(pre_products, suf_products)]

        # 前后缀分解 优化
        # 时间复杂度 O(n)
        # 空间复杂度 O(1) 「输出数组不被视为额外空间」

        suf_products = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suf_products[i] = suf_products[i + 1] * nums[i + 1]

        pre = 1
        for i in range(len(nums)):
            suf_products[i] *= pre
            pre *= nums[i]

        return suf_products


# @lc code=end
