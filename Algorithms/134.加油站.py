#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#


# @lc code=start
class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Brute-Force Search 超时
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)
        '''
        Time Limit Exceeded
        34/39 cases passed (N/A)
        '''
        # n = len(gas)
        # for i in range(n):
        #     rest = gas[i] - cost[i]
        #     index = (i + 1) % n
        #     while rest >= 0 and index != i:
        #         rest += gas[index] - cost[index]
        #         index = (index + 1) % n
        #     if rest >= 0 and index == i: return i
        # return -1

        # 贪心 版本一
        '''
        39/39 cases passed (62 ms)
        Your runtime beats 94.65 % of python3 submissions
        Your memory usage beats 16.38 % of python3 submissions (22.6 MB)
        '''
        # n = len(gas)
        # gaps = []
        # for i in range(n):
        #     gaps.append(gas[i] - cost[i])
        # index = -1
        # count = 0
        # for i in range(n):
        #     if count + gaps[i] < 0:
        #         index = -1
        #         count = 0
        #         continue
        #     if index == -1:
        #         index = i
        #     count += gaps[i]
        # for i in range(index):
        #     if count + gaps[i] < 0:
        #         index = -1
        #         count = 0
        #         break
        #     count += gaps[i]
        # return index

        # 贪心 版本二 实际上不一定是贪心算法
        # NOTE 没太搞懂, 为什么从后往前并累加
        '''
        39/39 cases passed (62 ms)
        Your runtime beats 94.65 % of python3 submissions
        Your memory usage beats 16.38 % of python3 submissions (22.6 MB)
        '''
        import sys
        curSum = 0
        minSum = sys.maxsize
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            minSum = min(minSum, curSum)

        if curSum < 0: return -1
        if minSum >= 0: return 0

        for i in range(len(gas) - 1, -1, -1):
            minSum += gas[i] - cost[i]
            if minSum >= 0:
                return i
        return -1


# @lc code=end
