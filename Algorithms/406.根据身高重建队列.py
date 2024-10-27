#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#


# @lc code=start
class Solution:

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 贪心
        '''
        36/36 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 79.35 % of python3 submissions (16.8 MB)
        '''
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue


# @lc code=end
