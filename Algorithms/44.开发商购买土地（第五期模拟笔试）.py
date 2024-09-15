# 44.开发商购买土地（第五期模拟笔试）
# 转置生成器,节省内存
# 方法一: 转置矩阵 + 前缀和 + 对比差值
def transpose_generator(arr):
    return (list(row) for row in zip(*arr))

import sys
ans = sys.maxsize
n, m = input().split()
arr = []
for i in range(int(n)):
    arr.append(list(map(int, input().split())))

sums_row = [sum(i) for i in arr]
pre_sums_row = [0]
for i in range(len(sums_row)):
    pre_sums_row.append(sums_row[i]+pre_sums_row[-1])
for i in range(len(pre_sums_row)-1):
    difference = abs(pre_sums_row[-1] - 2*pre_sums_row[i])
    if difference <= ans:
        ans = difference

# transpose_arr = [list(row) for row in zip(*arr)]
transpose_arr = transpose_generator(arr)
sums_col = [sum(i) for i in transpose_arr]
pre_sums_col = [0]
for i in range(len(sums_col)):
    pre_sums_col.append(sums_col[i]+pre_sums_col[-1])
for i in range(len(pre_sums_col)-1):
    difference = abs(pre_sums_col[-1] - 2*pre_sums_col[i])
    if difference <= ans:
        ans = difference
print(ans)


        