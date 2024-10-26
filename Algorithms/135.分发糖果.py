#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#


# @lc code=start
class Solution:

    def candy(self, ratings: List[int]) -> int:

        # NOTE 重点题目
        # 贪心 双贪心
        '''
        48/48 cases passed (18 ms)
        Your runtime beats 96.91 % of python3 submissions
        Your memory usage beats 83.95 % of python3 submissions (18.6 MB)
        '''
        candyVec = [1]
        for i in range(1, len(ratings)):
            cur_candy = candyVec[-1] + 1 if ratings[i] > ratings[i - 1] else 1
            candyVec.append(cur_candy)

        for i in range(len(ratings) - 2, -1, -1):
            cur_candy = candyVec[i + 1] + 1 if ratings[i] > ratings[i +
                                                                    1] else 1
            candyVec[i] = max(candyVec[i], cur_candy)

        return sum(candyVec)


# @lc code=end
