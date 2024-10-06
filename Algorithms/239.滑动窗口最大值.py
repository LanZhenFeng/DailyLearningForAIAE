#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums:  List[int], k: int) -> List[int]:
        '''
        51/51 cases passed (195 ms)
        Your runtime beats 92.67 % of python3 submissions
        Your memory usage beats 31.94 % of python3 submissions (30.4 MB)
        '''
        from collections import deque
        ans = []
        queue = deque()
        
        for i in range(len(nums)):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            if i >= k-1:
                ans.append(queue[0])
                if nums[i-k+1] == queue[0]:
                    queue.popleft()
        return ans

# @lc code=end

