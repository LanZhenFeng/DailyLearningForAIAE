#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#


# @lc code=start
class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        # 回溯 + 剪枝
        '''
        146/146 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 48.55 % of python3 submissions (16.4 MB)
        '''
        def backtracking(s, start, path, ans, level) -> None:
            if len(path) == 4:
                # print(path)
                pathSt = '.'.join(path)
                if len(pathSt) == len(s) + 3:
                    ans.append(pathSt)
                return None

            for i in range(start, start + 3):
                if i >= len(s): break
                cur_str = s[start:i + 1]
                if len(s) - len(cur_str) - start > 3 * (level - 1): continue
                if cur_str[0] == "0" and len(cur_str) != 1: break
                if 0 <= int(cur_str) <= 255:
                    # print(f'{s[start:i+1]}')
                    path.append(s[start:i + 1])
                    backtracking(s, i + 1, path, ans, level - 1)
                    path.pop()
                else:
                    break

        ans = []
        backtracking(s, 0, [], ans, 4)

        return ans


# @lc code=end
