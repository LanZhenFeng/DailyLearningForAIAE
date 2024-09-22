#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        # 方法一：暴力遍历 iteration=7是通过所有测试用例的最小迭代数
        '''
        420/420 cases passed (32 ms)
        Your runtime beats 92.41 % of python3 submissions
        Your memory usage beats 67.49 % of python3 submissions (16.3 MB)
        '''
        # iteration = 7
        # while n != 1 and iteration:
        #     n_str = str(n)
        #     nums = []
        #     nums.extend(n_str)
        #     n = sum(list(map(lambda x:int(x)**2, nums)))
        #     iteration -= 1
        # if n == 1:
        #     return True
        # else:
        #     return False
        
        # 方法二：使用集合
        '''420/420 cases passed (37 ms)
        Your runtime beats 76.36 % of python3 submissions
        Your memory usage beats 43.84 % of python3 submissions (16.4 MB)
        '''
        # record = set()

        # while True:
        #     n = self.get_sum(n)
        #     if n == 1:
        #         return True
            
        #     if n in record:
        #         return False
        #     else:
        #         record.add(n)

        # 方法二v2：使用集合
        '''
        420/420 cases passed (29 ms)
        Your runtime beats 97.2 % of python3 submissions
        Your memory usage beats 15.18 % of python3 submissions (16.4 MB)
        '''
        # record = set()
        # while n not in record:
        #     record.add(n)
        #     new_num = 0
        #     n_str = str(n)
        #     for i in n_str:
        #         new_num+=int(i)**2
        #     if new_num==1: 
        #         return True
        #     else: 
        #         n = new_num
        # return False

        # 方法二v3：使用集合
        '''
        420/420 cases passed (36 ms)
        Your runtime beats 80.28 % of python3 submissions
        Your memory usage beats 72.89 % of python3 submissions (16.3 MB)
        '''
        # seen = set()
        # while n != 1:
        #     n = sum(int(i) ** 2 for i in str(n))
        #     if n in seen:
        #         return False
        #     seen.add(n)
        # return True

        # 方法三：使用数组
        '''
        420/420 cases passed (41 ms)
        Your runtime beats 53.59 % of python3 submissions
        Your memory usage beats 68.22 % of python3 submissions (16.3 MB)
        '''
        # record = []
        # while n not in record:
        #     record.append(n)
        #     new_num = 0
        #     n_str = str(n)
        #     for i in n_str:
        #         new_num+=int(i)**2
        #     if new_num==1: return True
        #     else: n = new_num
        # return False

        # 方法三v2：使用数组
        '''
        420/420 cases passed (40 ms)
        Your runtime beats 60.19 % of python3 submissions
        Your memory usage beats 5.33 % of python3 submissions (16.5 MB)
        '''
        seen = []
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in seen:
                return False
            seen.append(n)
        return True
    
        # 方法三：快慢指针
        '''
        420/420 cases passed (38 ms)
        Your runtime beats 72.91 % of python3 submissions
        Your memory usage beats 21.01 % of python3 submissions (16.4 MB)
        '''
        slow = n
        fast = n
        while self.get_sum(fast) != 1 and self.get_sum(self.get_sum(fast)):
            slow = self.get_sum(slow)
            fast = self.get_sum(self.get_sum(fast))
            if slow == fast:
                return False
        return True
        

    def get_sum(self,n: int) -> int: 
        new_num = 0
        while n:
            n, r = divmod(n, 10)
            new_num += r ** 2
        return new_num
        
# @lc code=end

