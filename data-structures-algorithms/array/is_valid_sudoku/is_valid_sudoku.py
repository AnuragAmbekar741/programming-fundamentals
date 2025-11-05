from re import T


def is_valid_sudoku(board:list[list[str]])->bool:
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            cell = board[i][j]

            if cell == '.':
                continue

            if cell in rows[i]:
                return False
            rows[i].add(cell)

            if cell in columns[j]:
                return False
            columns[j].add(cell)

            box_index = (i//3)*3+(j//3)
            if cell in boxes[box_index]:
                return False
            boxes[box_index].add(cell)

    return True


board = [
    ["5","3",".",".","7",".",".",".","."]
   ,["6",".",".","1","9","5",".",".","."]
   ,[".","9","8",".",".",".",".","6","."]
   ,["8",".",".",".","6",".",".",".","3"]
   ,["4",".",".","8",".","3",".",".","1"]
   ,["7",".",".",".","2",".",".",".","6"]
   ,[".","6",".",".",".",".","2","8","."]
   ,[".",".",".","4","1","9",".",".","5"]
   ,[".",".",".",".","8",".",".","7","9"]
   ]

print(is_valid_sudoku(board))
