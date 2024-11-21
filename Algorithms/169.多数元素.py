#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#


# @lc code=start
class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        # 使用字典统计
        # counter = {}
        # for num in nums:
        #     counter[num] = counter.get(num, 0) + 1

        # for k, v in counter.items():
        #     if v > int(len(nums) / 2):
        #         return k

        # 使用字典统计
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        # from collections import Counter
        # counter = Counter(nums)

        # # for k in counter:
        # #     if counter[k] > int(len(nums) / 2):
        # #         return k
        # return max(counter.keys(), key=counter.get)

        # 排序
        # 如果将数组 nums 中的所有元素按照单调递增或单调递减的顺序排序，那么下标为⌊2/n⌋的元素（下标从 0 开始）一定是众数。
        # 时间复杂度 O(nlogn)
        # 空间复杂度 O(logn) sort  自己写堆排 O(1)
        # nums.sort()
        # return nums[int(len(nums) / 2)]

        # 随机化
        # 该题特殊情况 时间复杂度为O(n)
        # 空间复杂度 O(1)
        # majority_count = int(len(nums) / 2)
        # while True:
        #     candidate = random.choice(nums)
        #     if sum(1 for num in nums if num == candidate) > majority_count:
        #         return candidate

        # 分治法
        # 时间复杂度 O(nlogn)
        # 空间复杂度 O(logn)

        # def majorityElement_rec(l, r):
        #     if l == r: return nums[l]

        #     mid = (r - l) // 2 + l
        #     left = majorityElement_rec(l, mid)
        #     right = majorityElement_rec(mid+1, r)

        #     if left == right:
        #         return left

        #     left_count = sum(1 for i in range(l, r+1) if nums[i] == left)
        #     right_count = sum(1 for i in range(l, r+1) if nums[i] == right)

        #     return left if left_count > right_count else right

        # return majorityElement_rec(0, len(nums) - 1)

        # 摩尔投票
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


# @lc code=end
