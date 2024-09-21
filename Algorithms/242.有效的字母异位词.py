#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 方法一：字典
        # 时间复杂度：O(n)
        '''
        49/49 cases passed (54 ms)
        Your runtime beats 40.58 % of python3 submissions
        Your memory usage beats 16.47 % of python3 submissions (16.6 MB)
        '''
        # i = 0
        # dict = {}
        # while i<len(s):
        #     if not dict.get(s[i], None):
        #         dict[s[i]] = 1
        #     else:
        #         dict[s[i]] = dict[s[i]] + 1
        #     i += 1
        # i = 0
        # dict2 = {}
        # while i<len(t):
        #     if not dict2.get(t[i], None):
        #         dict2[t[i]] = 1
        #     else:
        #         dict2[t[i]] = dict2[t[i]] + 1
        #     i += 1
        # keys1 = dict.keys()
        # keys2 = dict2.keys()
        # if keys1 == keys2:
        #     flag = True
        #     for key in keys1:
        #         if dict[key] != dict2[key]:
        #             flag = False
        #             break
        #     return flag
        # return False
    
        # 方法一v2：defaultdict
        # 时间复杂度：O(n)
        '''
        49/49 cases passed (47 ms)
        Your runtime beats 73.44 % of python3 submissions
        Your memory usage beats 19.18 % of python3 submissions (16.6 MB)
        '''
        # if len(s) != len(t):
        #     return False
        # from collections import defaultdict
        # dict1 = defaultdict(int)
        # dict2 = defaultdict(int)

        # for i in range(len(s)):
        #     dict1[s[i]] += 1
        #     dict2[t[i]] += 1
        # return dict1 == dict2

        # 方法二：利用列表作为哈希表
        # 时间复杂度：O(n)
        '''
        49/49 cases passed (50 ms)
        Your runtime beats 59.14 % of python3 submissions
        Your memory usage beats 42.91 % of python3 submissions (16.5 MB)
        '''
        # if len(s) != len(t):
        #     return False

        # record = [0] * 26
        # for i in range(len(s)):
        #     record[ord(s[i]) - ord('a')] += 1

        # for i in range(len(t)):
        #     record[ord(t[i]) - ord('a')] -= 1

        # for r in record:
        #     if r != 0: 
        #         return False
        # return True
    
        # 方法三：使用Counter
        # 时间复杂度：O(n)
        '''
        49/49 cases passed (53 ms)
        Your runtime beats 44.49 % of python3 submissions
        Your memory usage beats 17.49 % of python3 submissions (16.6 MB)
        '''
        # from collections import Counter
        # counter = Counter()
        # for i in range(len(s)):
        #     counter[ord(s[i]) - ord('a')] += 1

        # for i in range(len(t)):
        #     counter[ord(t[i]) - ord('a')] -= 1
        #     if counter[ord(t[i]) - ord('a')] == 0:
        #         del counter[ord(t[i]) - ord('a')]
        # for i in s:
        #     counter[i] += 1
        # for j in t:
        #     counter[j] -= 1
        #     if counter[j] == 0:
        #         del counter[j]
        
        # return True if len(counter) == 0 else False
    
        # 方法三v2：直接初始化计数器
        # 时间复杂度：O(n)
        '''
        49/49 cases passed (42 ms)
        Your runtime beats 90.26 % of python3 submissions
        Your memory usage beats 76.63 % of python3 submissions (16.4 MB)
        '''
        from collections import Counter
        return Counter(s) == Counter(t)


            
# @lc code=end

