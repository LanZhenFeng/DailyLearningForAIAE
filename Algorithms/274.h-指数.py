#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 排序
        # 时间复杂度 O(nlogn)
        # 空间复杂度 O(logn)
        # citations.sort()
        # h_index = 0
        # n = len(citations)
        # for i in range(n-1, -1, -1):
        #     if n-i <= citations[i]:
        #         h_index = n-i
        # return h_index

        # 计数排序
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        # n = len(citations)
        # count = [0] * (n+1)
        
        # for citation in citations:
        #     count[min(citation, n)] += 1
        
        # h_index = 0
        # for i in range(n, -1, -1):
        #     h_index += count[i]
        #     if h_index >= i:
        #         return i
        # return 0

        # 二分
        # 时间复杂度 O(nlogn)
        # 空间复杂度 O(1)
        left = 0
        right = len(citations)
        count = 0
        while left < right:
            mid = (left+right+1) >> 1
            count = 0
            for i in range(len(citations)):
                if citations[i] >= mid:
                    count += 1
            
            if count >= mid:
                left = mid
            else:
                right = mid-1
            
        return left
# @lc code=end

