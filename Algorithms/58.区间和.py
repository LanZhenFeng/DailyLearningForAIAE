# 58.区间和 （第九期模拟笔试） by Kamacoder
# 需使用前缀和,否则容易超时
# 方法一: 使用try-except显式检测EOF信号
# lens = int(input())
# nums = []
# for i in range(lens):
#     nums.append(int(input()))
# cumsum = [0]
# for i in range(lens):
#     cumsum.append(nums[i]+cumsum[-1])
# try:
#     while True:
#         inp = input()
#         if not inp:
#             break
#         ab = inp.split()
#         a = int(ab[0])
#         b = int(ab[1])
#         res = cumsum[b+1] - cumsum[a]
#         print(res)
# except EOFError:
#    pass

# 方法二: 使用sys.stdin隐式检测EOF信号
import sys
read = sys.stdin.read

lens = int(input())
nums = []
for i in range(lens):
    nums.append(int(input()))
cumsum = [0]
for i in range(lens):
    cumsum.append(nums[i]+cumsum[-1])

index = 0
lines = read().splitlines()
for line in lines:
    a, b = line.split()
    res = cumsum[int(b) + 1] - cumsum[int(a)]
    print(res)

