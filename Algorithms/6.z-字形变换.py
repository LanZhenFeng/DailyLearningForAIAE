#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#


# @lc code=start
class Solution:

    def convert(self, s: str, numRows: int) -> str:
        # if 4
        # 0     6       12
        # 1   5 7    11 13
        # 2 4   8 10    14
        # 3     9       15
        # if 3
        # 0   4   8     12
        # 1 3 5 7 9  11 13
        # 2   6   10    14
        # 模拟
        # 时间复杂度 O(m * n)
        # 空间复杂度 O(n)
        # if numRows == 1: return s
        # ans = []
        # len_s = len(s)
        # base = numRows+numRows-2
        # for row in range(numRows):
        #     for i in range(len_s):
        #         if i%base == row or i%base == base - row:
        #             ans.append(s[i])

        # return "".join(ans)

        # 模拟优化 1
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        # if numRows == 1: return s
        # ans = [[] for _ in range(numRows)]
        # i, flag = 0, -1
        # for c in s:
        #     ans[i].append(c)
        #     if i == 0 or i == numRows - 1: flag = -flag
        #     i += flag
        # return "".join(["".join(row) for row in ans])

        # 模拟优化 2
        # 时间复杂度 O(n)
        # 空间复杂度 O(1)

        len_s = len(s)
        if numRows == 1 or numRows >= len_s: return s
        base = numRows + numRows - 2
        ans = []
        for row in range(numRows):
            for j in range(0, len_s - row, base):
                ans.append(s[j + row])
                if 0 < row < numRows - 1 and j + base - row < len_s:
                    ans.append(s[j + base - row])
        return ''.join(ans)


# @lc code=end
