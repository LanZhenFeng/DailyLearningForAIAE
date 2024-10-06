#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        21/21 cases passed (40 ms)
        Your runtime beats 86.91 % of python3 submissions
        Your memory usage beats 36.2 % of python3 submissions (20 MB)
        '''
        from collections import Counter
        ans = []
        c = Counter(nums)
        keyvalue = c.most_common(k)
        for i in keyvalue:
            ans.append(i[0])
        # print(ans)
        return ans
# @lc code=end

