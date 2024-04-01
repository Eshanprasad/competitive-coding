def is_row_marked(mat, row, col):
    return all(mat[row][i] is None for i in range(len(mat)))

def is_col_marked(mat, row, col):
    return all(mat[i][col] is None for i in range(len(mat)))

def bingo_game(mat, arr):
    n = len(mat)
    for num in arr:
        for i in range(n):
            for j in range(n):
                if mat[i][j] == num:
                    mat[i][j] = None
                    if is_row_marked(mat, i, j):
                        return num
                    if is_col_marked(mat,i, j):
                        return num
    return None
n = 3
mat = [[3, 1, 8],
       [4, 6, 2],
       [7, 5, 9]]  # Initial matrix
arr = [3,4,6,9,5,7,9]  # Numbers called during the game
print(bingo_game(mat, arr))