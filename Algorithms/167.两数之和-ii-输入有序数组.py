#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 暴力 超时
        # 时间复杂度 O(n^2) ❌
        # 空间复杂度 O(1) ✅
        # for idx1 in range(len(numbers)-1):
        #     for idx2 in range(idx1+1, len(numbers)):
        #         if numbers[idx2] + numbers[idx1] == target:
        #             return [idx1+1, idx2+1]
        # return

        # 哈希表
        # 时间复杂度 O(n) ✅
        # 空间复杂度 O(n) ❌ 题目要求只使用常量级的额外空间
        # dic = collections.defaultdict(list)
        # for i in range(len(numbers)):
        #     dic[numbers[i]].append(i)

        # for i in range(len(numbers)):
        #     if target - numbers[i] in dic:
        #         for j in dic[target - numbers[i]]:
        #             if j != i:
        #                 return [i+1, j+1]


        # 二分查找
        # 时间复杂度 O(nlogn) ✅
        # 空间复杂度 O(1) ✅
        # for idx1 in range(len(numbers)):
        #     low, high = idx1 + 1, len(numbers) - 1
        #     while low <= high:
        #         mid = (high - low) // 2 + low
        #         if numbers[mid] == target - numbers[idx1]:
        #             return [idx1+1, mid+1]
        #         elif numbers[mid] > target - numbers[idx1]:
        #             high = mid - 1
        #         else:
        #             low = mid + 1
        # return [-1, -1]

        # 二分查找库函数
        # 时间复杂度 O(nlogn) ✅
        # 空间复杂度 O(1) ✅
        import bisect
        for idx1 in range(len(numbers)-1):
            complement = target-numbers[idx1]
            idx2 = bisect.bisect_left(numbers, complement, idx1+1, len(numbers))
            if idx2 < len(numbers) and complement == numbers[idx2]:
                return [idx1+1, idx2+1]
        return [-1, -1]

        # 双指针
        # 时间复杂度 O(n) ✅
        # 空间复杂度 O(1) ✅
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        return [-1, -1]
# @lc code=end

