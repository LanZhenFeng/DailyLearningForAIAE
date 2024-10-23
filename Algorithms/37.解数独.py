#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#


# @lc code=start
class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        6/6 cases passed (15 ms)
        Your runtime beats 99.94 % of python3 submissions
        Your memory usage beats 9.97 % of python3 submissions (16.6 MB)
        '''
        # rows
        row_opt_nums = [
            set([str(num) for num in range(1, 10)]) for i in range(9)
        ]
        col_opt_nums = [
            set([str(num) for num in range(1, 10)]) for i in range(9)
        ]
        block_opt_nums = [
            set([str(num) for num in range(1, 10)]) for i in range(9)
        ]
        for i in range(9):
            for j in range(9):
                if board[i][j] in row_opt_nums[i]:
                    row_opt_nums[i].discard(board[i][j])
                if board[i][j] in col_opt_nums[j]:
                    col_opt_nums[j].discard(board[i][j])
                block_i = i // 3
                block_j = j // 3
                block_index = block_i * 3 + block_j
                if board[i][j] in block_opt_nums[block_index]:
                    block_opt_nums[block_index].discard(board[i][j])
        # print(block_opt_nums)
        # cols
        def getIntersection(i, j):
            block_i = i // 3
            block_j = j // 3
            block_index = block_i * 3 + block_j
            rc = row_opt_nums[i].intersection(col_opt_nums[j])
            rcb = rc.intersection(block_opt_nums[block_index])
            return rcb

        def backtracking(board, pos):
            i, j = divmod(pos, 9)
            while i < 9 and board[i][j] != ".":
                if j < 8:
                    j += 1
                elif j == 8:
                    i += 1
                    j = 0
            if i == 9: return True
            block_i = i // 3
            block_j = j // 3
            block_index = block_i * 3 + block_j
            opt_nums = getIntersection(i, j)
            # print(i, j, opt_nums)
            for opt_num in opt_nums:
                board[i][j] = opt_num
                row_opt_nums[i].discard(opt_num)
                col_opt_nums[j].discard(opt_num)
                block_opt_nums[block_index].discard(opt_num)
                res = backtracking(board, i * 9 + j + 1)
                if res: return True
                row_opt_nums[i].add(opt_num)
                col_opt_nums[j].add(opt_num)
                block_opt_nums[block_index].add(opt_num)
                board[i][j] = "."
            return False

        backtracking(board, 0)
        return board


# @lc code=end
