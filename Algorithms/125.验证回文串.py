#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 筛选+判断
        # 时间复杂度 O(∣s∣)
        # 空间复杂度 O(∣s∣)
        # new_s = []
        # for char in s:
        #     if char.isalnum():
        #         new_s.append(char.lower())
        
        # return new_s[::-1] == new_s

        # 筛选+判断 双指针
        # 时间复杂度 O(∣s∣)
        # 空间复杂度 O(∣s∣)
        # new_s = []
        # for char in s:
        #     if char.isalnum():
        #         new_s.append(char.lower())
        
        # left = 0
        # right = len(new_s) - 1
        # while left < right:
        #     if new_s[left] == new_s[right]:
        #         left += 1
        #         right -= 1
        #     else:
        #         return False
        # return True

        # 不筛选 直接判断
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
# @lc code=end

