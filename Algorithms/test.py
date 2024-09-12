from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        offset = 0
        lens = len(nums)
        i = 0
        while i < lens:
            print(nums)
            if i+offset >= lens:
                print(f"break:{i}")
                break
            if val == nums[i]:
                print(f"pop:{i}")
                nums.pop(i)
                i = i-1
                offset += 1
            i = i+1
        return len(nums)
        # k = 0
        # f = 0
        # offset = 0
        # last_index = len(nums)
        # for i in range(last_index):
        #     if nums[(i+offset)%last_index] == val:
        #         while i+offset <= last_index - 1:
        #             k += 1
        #             print(i+offset)
        #             offset += 1
        #             if nums[(i+offset)%last_index] != val:
        #                 break
        #     nums[i] = nums[(i+offset)%last_index]
        #     # print(i, nums[i])
        #         # nums[i] = nums[f]
        #         # repeat += 1
        #         # # last_index -= 1
        # return last_index - k

solution = Solution()

nums = [3,2,2,3]
val = 3
expectedNums = [0,1,4,0,3,0,4,2]

k = solution.removeElement(nums, val)
print(k,nums)
# assert k == len(expectedNums)
# nums.sort()
# sort(nums, 0, k); // 排序 nums 的前 k 个元素
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }

