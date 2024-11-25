#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        # 模拟
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)
        enum = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        ans = 0
        i = 0
        while i < len(s) - 1:
            if enum[s[i+1]] > enum[s[i]]:
                ans += enum[s[i+1]] - enum[s[i]]
                i += 1
            else:
                ans += enum[s[i]]
            i += 1
        if i < len(s):
            ans += enum[s[i]]
        return ans
# @lc code=end

