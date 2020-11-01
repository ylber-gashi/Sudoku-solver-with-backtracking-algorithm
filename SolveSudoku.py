def print_board(table):
    for i in range(9):
        if(i % 3 == 0 and i != 0):
            print("- - - - - - - - - - - - ")
        for j in range(9):
            if(j%3 == 0 and j != 0):
                print(" | ", end="")

            if(j==8):
                print(table[i][j])
            else:
                print(str(table[i][j]) + " ", end="")

def is_empty(table):
    for x in range(9):
        for y in range(9):
            if(table[x][y] == 0):
                return (x,y)

    return None

def is_valid(nr, loc, table):
    # row check
    for y in range(9):
        if(table[loc[0]][y] == nr and y != loc[1]):
            return False

    # column check
    for x in range(9):
        if(table[x][loc[1]] == nr and x != loc[0]):
            return False

    box_x = loc[0] // 3
    box_y = loc[1] // 3

    for x in range(box_x * 3, box_x*3 + 3):
        for y in range(box_y*3, box_y*3 + 3):
            if(table[x][y] == nr and (x,y) != loc):
                return False
    return True

def solve_sudoku(table):
    if(not is_empty(table)):
        return True
    else:
        x,y = is_empty(table)

    for i in range(1,10):
        if(is_valid(i, (x,y), table)):
            table[x][y] = i

            if(solve_sudoku(table)):
                return True
            else:
                table[x][y] = 0
    return False


table = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
print("The unsolved Sudoku table: ")
print_board(table)
solve_sudoku(table)
print("__________________________")
print("The solved Sudoku table: ")
print_board(table)
