def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col, n):
 
    for i in range(row):
        if board[i][col] == 'Q':
            return False

   
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

   
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
       
        solutions.append(["".join(r) for r in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = '.'  # Backtrack

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions


n = int(input("Enter the value of N: "))
solutions = solve_n_queens(n)
print(f"Total solutions for {n}-Queens: {len(solutions)}\n")
for sol in solutions:
    for row in sol:
        print(row)
    print()
