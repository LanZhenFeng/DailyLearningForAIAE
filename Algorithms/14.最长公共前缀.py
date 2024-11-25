#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 遍历 横向搜索
        # 时间复杂度：O(mn)，其中 m 为 strs 的长度，n 为 strs 中最短字符串的长度。
        # 空间复杂度：O(1)。返回值不计入。
        # first_str = strs[0]
        # len_ans = len(first_str)

        # for i in range(1, len(strs)):
        #     cur_str = strs[i]
        #     j = 0
        #     min_len = min(len(cur_str), len_ans)
        #     while j < min_len:
        #         if cur_str[j] == first_str[j]:
        #             j += 1
        #         else:
        #             break
        #     len_ans = min(len_ans, j)
        #     if len_ans == 0:
        #         return ""
        # return first_str[:len_ans]

        # 遍历 纵向搜索
        # 时间复杂度：O(mn)
        # 空间复杂度：O(1)
        first_str = strs[0]
        for i, c in enumerate(first_str):
            for s in strs:
                if i == len(s) or s[i] != c:
                    return first_str[:i]
        return first_str
# @lc code=end

