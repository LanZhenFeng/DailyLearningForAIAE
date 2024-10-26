#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#


# @lc code=start
class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        '''
        61/61 cases passed (3 ms)
        Your runtime beats 99.02 % of python3 submissions
        Your memory usage beats 22.17 % of python3 submissions (20.6 MB)
        '''
        if bills[0] != 5: return False

        nums_5 = 0
        nums_10 = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                nums_5 += 1
            elif bills[i] == 10:
                if nums_5 < 1:
                    return False
                nums_5 -= 1
                nums_10 += 1
            elif bills[i] == 20:
                if nums_10 >= 1 and nums_5 >= 1:
                    nums_5 -= 1
                    nums_10 -= 1
                elif nums_5 >= 3:
                    nums_5 -= 3
                else:
                    return False

        return True


# @lc code=end
