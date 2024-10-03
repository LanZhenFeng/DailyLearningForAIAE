#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        61/61 cases passed (47 ms)
        Your runtime beats 22.65 % of python3 submissions
        Your memory usage beats 74.05 % of python3 submissions (16.4 MB)
        '''
        # ans = []
        # left = 0
        # right = len(s) - 1
        # while s[left].isspace():
        #     left += 1
        # while s[right].isspace():
        #     right -= 1
        # while left <= right:
        #     index = right
        #     while left < index and not s[index-1].isspace():
        #         index -= 1
        #         # if index == left:
        #         #     break
        #     ans.append(s[index:right+1])
        #     while s[index-1].isspace():
        #         index -= 1
        #     right = index - 1
        # return " ".join(ans)

        # 先删除空白，然后整个反转，最后单词反转。 因为字符串是不可变类型，所以反转单词的时候，需要将其转换成列表，然后通过join函数再将其转换成列表，所以空间复杂度不是O(1)
        '''
        61/61 cases passed (31 ms)
        Your runtime beats 94.85 % of python3 submissions
        Your memory usage beats 81.83 % of python3 submissions (16.4 MB)
        '''
        # 删除前后空白
        # s = s.strip()
        # # 反转整个字符串
        # s = s[::-1]
        # # 将字符串拆分为单词，并反转每个单词
        # s = ' '.join(word[::-1] for word in s.split())
        # return s


        # 拆分字符串 + 反转列表
        '''
        61/61 cases passed (29 ms)
        Your runtime beats 97.4 % of python3 submissions
        Your memory usage beats 63.52 % of python3 submissions (16.5 MB)
        '''
        s = s.split()
        s = s[::-1]
        s = ' '.join(s)
        return s
        
# @lc code=end

