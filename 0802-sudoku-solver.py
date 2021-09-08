"""
802. Sudoku Solver
Hard
https://leetcode.com/problems/sudoku-solver/

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""
from typing import List


class Solution:
    empty = "."

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.dfs(board, 0, 0)

    # @return True/False
    def dfs(self, board, row, col):
        size = len(board)

        # exit case
        if row == size:
            return True
        # next row
        if col == size:
            return self.dfs(board, row+1, 0)
        # not empty
        if board[row][col] != self.empty:
            return self.dfs(board, row, col+1)

        # valid indices
        for num in range(1, size+1):
            # leetcode input is str mf!
            num = str(num)

            if not self.is_valid(board, row, col, num):
                continue

            board[row][col] = num

            if self.dfs(board, row, col+1):
                return True

            # backtrack
            board[row][col] = self.empty

        return False

    def is_valid(self, board, row, col, num):
        for i in range(len(board)):
            # check row
            if board[i][col] == num:
                return False
            # check col
            if board[row][i] == num:
                return False
            # check subgrid
            if board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] == num:
                return False

        return True


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    Solution().solveSudoku(board)
    expected = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
    ]
    print(f"\noutput\t\t{board}")
    print(f"expected\t{expected}")
    print(board == expected)
