#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#


# @lc code=start
class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 普通回溯 超时
        '''
        Time Limit Exceeded
        80/81 cases passed (N/A)
        '''

        # def backtracking(tickets, path, ans, used):
        #     if len(path) == len(tickets) + 1:
        #         ans.append(path[:])
        #         return True

        #     for i in range(len(tickets)):
        #         if used[i]: continue
        #         if path and tickets[i][0] != path[-1]: continue
        #         path.append(tickets[i][1])
        #         used[i] = True
        #         res = backtracking(tickets, path, ans, used)
        #         if res:
        #             return True
        #         used[i] = False
        #         path.pop()

        # ans = []
        # used = [False] * len(tickets)
        # tickets = sorted(tickets, key=lambda item: item[1])
        # backtracking(tickets, ["JFK"], ans, used)
        # return ans[0]

        # 回溯 + 字典 + 可达性剪枝 (NOTE 还是不太明白)
        '''
        81/81 cases passed (0 ms)
        Your runtime beats 100 % of python3 submissions
        Your memory usage beats 73.86 % of python3 submissions (16.6 MB)
        '''

        def backtracking(adj_dic, from_, ans):
            while adj_dic[from_]:
                next_ = adj_dic[from_].pop()
                backtracking(adj_dic, next_, ans)

            ans.append(from_)
            print(ans)

        ans = []
        tickets = sorted(tickets, key=lambda item: item[1], reverse=True)
        from collections import defaultdict
        adj_dic = defaultdict(list)
        for u, v in tickets:
            adj_dic[u].append(v)
        backtracking(adj_dic, "JFK", ans)
        return ans[::-1]


# @lc code=end
