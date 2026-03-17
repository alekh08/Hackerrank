import sys

def get_moves(pieces_dict, is_white, board):
    """Generates all valid moves for the given player's pieces."""
    valid_moves = []
    color = 1 if is_white else -1
    
    for pid, (ptype, x, y) in pieces_dict.items():
        dirs = []
        is_knight = False
        
        # Define directional vectors based on piece type
        if ptype == 'N':
            dirs = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
            is_knight = True
        elif ptype == 'R':
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        elif ptype == 'B':
            dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        elif ptype == 'Q':
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            
        for dx, dy in dirs:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                
                # Check 4x4 board boundaries
                if 0 <= nx < 4 and 0 <= ny < 4:
                    target = board[ny][nx]
                    if target is None:
                        # Empty square
                        valid_moves.append((pid, ptype, x, y, nx, ny, None))
                    elif target[0] == color:
                        # Blocked by friendly piece
                        break
                    else:
                        # Capture enemy piece
                        valid_moves.append((pid, ptype, x, y, nx, ny, target[1]))
                        break
                else:
                    break
                
                # Knights don't slide; break after evaluating one square per direction
                if is_knight:
                    break
                    
    return valid_moves


def solve(white_pieces, black_pieces, moves_left, is_white_turn, memo):
    """Minimax DFS to evaluate if White can force a win."""
    
    # 1. Base Win/Loss Conditions
    black_has_queen = any(ptype == 'Q' for ptype, x, y in black_pieces.values())
    if not black_has_queen: 
        return True  # White won
    
    white_has_queen = any(ptype == 'Q' for ptype, x, y in white_pieces.values())
    if not white_has_queen: 
        return False # Black won
        
    if moves_left == 0: 
        return False # White ran out of moves
    
    # 2. State definition for Memoization (avoids redundant calculations)
    w_state = tuple(sorted(white_pieces.values()))
    b_state = tuple(sorted(black_pieces.values()))
    state = (w_state, b_state, moves_left, is_white_turn)
    
    if state in memo:
        return memo[state]
        
    # 3. Build a 2D board state for fast collision detection
    board = [[None]*4 for _ in range(4)]
    for pid, (ptype, x, y) in white_pieces.items():
        board[y][x] = (1, pid, ptype)
    for pid, (ptype, x, y) in black_pieces.items():
        board[y][x] = (-1, pid, ptype)
        
    # 4. Recursive Minimax Search
    if is_white_turn:
        moves = get_moves(white_pieces, True, board)
        
        # Move Ordering Heuristic: Check captures first (especially Queen captures)
        moves.sort(key=lambda m: 100 if m[6] is not None and black_pieces[m[6]][0] == 'Q' else (10 if m[6] is not None else 0), reverse=True)
        
        ans = False
        for pid, ptype, x, y, nx, ny, cap_id in moves:
            new_w = white_pieces.copy()
            new_w[pid] = (ptype, nx, ny)
            new_b = black_pieces.copy()
            if cap_id is not None:
                del new_b[cap_id]
            
            # If ANY path leads to a White win, White forces a win (Logical OR)
            if solve(new_w, new_b, moves_left - 1, False, memo):
                ans = True
                break
                
        memo[state] = ans
        return ans
        
    else:
        moves = get_moves(black_pieces, False, board)
        
        # Move Ordering Heuristic: Check captures first
        moves.sort(key=lambda m: 100 if m[6] is not None and white_pieces[m[6]][0] == 'Q' else (10 if m[6] is not None else 0), reverse=True)
        
        ans = True
        for pid, ptype, x, y, nx, ny, cap_id in moves:
            new_b = black_pieces.copy()
            new_b[pid] = (ptype, nx, ny)
            new_w = white_pieces.copy()
            if cap_id is not None:
                del new_w[cap_id]
                
            # If ANY Black move successfully blocks the win, White fails (Logical AND)
            if not solve(new_w, new_b, moves_left - 1, True, memo):
                ans = False
                break
                
        memo[state] = ans
        return ans


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    g = int(input_data[0])
    idx = 1
    
    # Coordinate mappers
    col_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    
    for _ in range(g):
        w = int(input_data[idx])
        b = int(input_data[idx+1])
        m = int(input_data[idx+2])
        idx += 3
        
        white_pieces = {}
        for i in range(w):
            ptype = input_data[idx]
            col = col_map[input_data[idx+1]]
            row = int(input_data[idx+2]) - 1
            white_pieces[i] = (ptype, col, row)
            idx += 3
            
        black_pieces = {}
        for i in range(b):
            ptype = input_data[idx]
            col = col_map[input_data[idx+1]]
            row = int(input_data[idx+2]) - 1
            black_pieces[i] = (ptype, col, row)
            idx += 3
            
        memo = {}
        if solve(white_pieces, black_pieces, m, True, memo):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()
