#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#


# @lc code=start
class Solution:

    def partitionLabels(self, s: str) -> List[int]:
        # 贪心
        '''
        118/118 cases passed (3 ms)
        Your runtime beats 94.97 % of python3 submissions
        Your memory usage beats 71.34 % of python3 submissions (16.4 MB)
        '''
        # partions = []
        # from collections import defaultdict
        # intervals = defaultdict(list)
        # for i, si in enumerate(s):
        #     if len(intervals.get(si, list())) == 0:
        #         intervals[si].append(i)
        #         intervals[si].append(i)
        #     else:
        #         intervals[si][1] = i
        # sorted_intervals = sorted(intervals.values(), key=lambda item: item[0])

        # pr = 0
        # for l, r in sorted_intervals:
        #     if l > pr:
        #         pr = r
        #         partions.append(l)
        #     else:
        #         pr = max(pr, r)
        # partions.append(len(s))
        # for i in range(len(partions) - 1, 0, -1):
        #     partions[i] -= partions[i - 1]
        # return partions

        # 贪心 版本二
        '''
        118/118 cases passed (7 ms)
        Your runtime beats 53.7 % of python3 submissions
        Your memory usage beats 59.49 % of python3 submissions (16.4 MB)
        '''
        remotePos = [0] * 26
        for i in range(len(s)):
            remotePos[ord(s[i]) - ord('a')] = i
        l = 0
        r = 0
        partions = []
        for i in range(len(s)):
            r = max(r, remotePos[ord(s[i]) - ord('a')])
            if i == r:
                partions.append(r - l + 1)
                l = i + 1
        return partions


# @lc code=end
