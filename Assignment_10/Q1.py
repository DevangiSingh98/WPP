def print_board(board):
    
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col):
    
    for i in range(row):
        if board[i][col]: 
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)]:  
            return False
        if col + (row - i) < len(board) and board[i][col + (row - i)]:  
            return False
    return True

def solve_n_queens(board, row):
    
    if row == len(board):
        print_board(board) 
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = True  
            solve_n_queens(board, row + 1)  
            board[row][col] = False  

def eight_queens():
   
    board = [[False] * 8 for _ in range(8)]
    solve_n_queens(board, 0)

eight_queens()
