#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#


# @lc code=start
class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 贪心 小饼干优先
        # '''
        # 25/25 cases passed (15 ms)
        # Your runtime beats 99.78 % of python3 submissions
        # Your memory usage beats 12.05 % of python3 submissions (18.7 MB)
        # '''
        # ans = 0
        # g.sort()
        # s.sort()
        # i = 0
        # j = 0
        # while i < len(g) and j < len(s):
        #     while j < len(s) and s[j] < g[i]:
        #         j += 1
        #     if j == len(s): break
        #     else:
        #         j += 1
        #         i += 1
        #         ans += 1
        # return ans

        # 贪心 大饼干优先
        '''
        25/25 cases passed (15 ms)
        Your runtime beats 99.78 % of python3 submissions
        Your memory usage beats 12.05 % of python3 submissions (18.7 MB)
        '''
        # ans = 0
        # g.sort()
        # s.sort()
        # i = len(g) - 1
        # j = len(s) - 1
        # while i >= 0 and j >= 0:
        #     while i >= 0 and s[j] < g[i]:
        #         i -= 1
        #     if i < 0: break
        #     else:
        #         j -= 1
        #         i -= 1
        #         ans += 1
        # return ans

        # 栈 小饼干优先
        '''
        25/25 cases passed (19 ms)
        Your runtime beats 99.36 % of python3 submissions
        Your memory usage beats 5.08 % of python3 submissions (19 MB)
        '''
        # ans = 0
        # from collections import deque
        # childs = deque(sorted(g))
        # cookies = deque(sorted(s))
        # while childs and cookies:
        #     child = childs.popleft()
        #     cookie = cookies.popleft()
        #     if cookie >= child:
        #         ans += 1
        #     else:
        #         childs.appendleft(child)
        # return ans

        # 栈 大饼干优先
        '''
        25/25 cases passed (23 ms)
        Your runtime beats 98.74 % of python3 submissions
        Your memory usage beats 5.05 % of python3 submissions (19.3 MB)
        '''
        ans = 0
        from collections import deque
        childs = deque(sorted(g))
        cookies = deque(sorted(s))
        while childs and cookies:
            child = childs.pop()
            cookie = cookies.pop()
            if cookie >= child:
                ans += 1
            else:
                cookies.append(cookie)
        return ans


# @lc code=end
