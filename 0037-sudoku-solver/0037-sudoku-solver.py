class Solution:
    def solveSudoku(self, board):
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r//3)*3 + c//3].add(val)
        
        def backtrack(index):
            if index == len(empty):
                return True
            
            r, c = empty[index]
            box_id = (r//3)*3 + c//3
            
            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_id]:
                    
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_id].add(num)
                    
                    if backtrack(index + 1):
                        return True
                    
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_id].remove(num)
            
            return False
        
        backtrack(0)