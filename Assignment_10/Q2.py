import random

def is_safe(board, row, col):
   
    for i in range(row):
        if board[i] == col:
            return False
        
       
        if abs(board[i] - col) == abs(i - row):
            return False
    
    return True

def place_queens(n=8):
    board = [-1] * n  
    for row in range(n):
        valid_positions = [col for col in range(n) if is_safe(board, row, col)]
        if not valid_positions:
            return None 
        board[row] = random.choice(valid_positions)
    return board

def print_board(board):
    if not board:
        print("No valid solution found.")
        return
    
    n = len(board)
    for row in range(n):
        line = ['.'] * n
        line[board[row]] = 'Q'
        print(" ".join(line))
    print()


solution = None
while solution is None:
    solution = place_queens()

print("Randomly placed queens on the board:")
print_board(solution)
