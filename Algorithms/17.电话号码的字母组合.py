#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#


# @lc code=start
class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        # 回溯
        '''
        25/25 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 8.46 % of python3 submissions (16.5 MB)
        '''
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtracking(digits, indexSt, path, ans):
            if indexSt >= len(digits):
                if len(path):
                    pathSt = ''.join(path)
                    ans.append(pathSt)
                return
            number = digits[indexSt]
            for char in mapping[number]:
                path.append(char)
                backtracking(digits, indexSt + 1, path, ans)
                path.pop()

        ans = []
        backtracking(digits, 0, [], ans)
        return ans


# @lc code=end
