#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 使用字典
        '''
        129/129 cases passed (45 ms)
        Your runtime beats 95.7 % of python3 submissions
        Your memory usage beats 36.51 % of python3 submissions (16.6 MB)
        '''
        mdict = defaultdict(int)
        for m in magazine:
            mdict[m] += 1
        for r in ransomNote:
            if r in mdict:
                mdict[r] -= 1
                if mdict[r] == 0:
                    del mdict[r]
            else:
                return False
        return True


# @lc code=end

