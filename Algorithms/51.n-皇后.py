#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        mapping={}
        st = '.'*n
        for i in range(n):
            s=st[:i]+'Q'+st[i+1:]
            mapping[i]=s
        # print(mapping)
        
        def isValid(pos,path):
            offset=1
            for i in path[::-1]:
                if pos==i:
                    return False
                if pos==i+offset or pos==i-offset:
                    return False
                offset+=1
            return True

        def backtracking(n,path,ans,ban):
            if len(path)==n:
                temp=[mapping[i] for i in path]
                ans.append(temp)
            
            for i in range(n):
                if isValid(i,path):
                    
                    path.append(i)
                    backtracking(n,path,ans,ban)
                    path.pop()
                else:
                    continue
        
        ans=[]
        ban=set()
        backtracking(n,[],ans,ban)
        return ans

# @lc code=end

