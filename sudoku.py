
def solver(x):
    find = find_empty(x)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        # Checks if the number is valid
        if valid(x, i, (row, col)):
            # Adds the number onto the board
            x[row][col] = i
            
            if solver(x):
                return True
            # Resets the value if it fails to find a number.
            x[row][col] = 0
    return False



# Checks if there are dublicate numbers or numbers already plotted at pos.
def valid(x, num, pos):
    # Check row
    for i in range(len(x[0])):
        if x[pos[0]][i] == num and pos[1] != i:
            return False
        
    # Check column
    for i in range(len(x)):
        if x[i][pos[1]] == num and pos[0] != i:
            return False
        
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if x[i][j] == num and (i, j) != pos:
                return False
    return True

def print_board(x):
    for i in range(len(x)):
        if i % 3 == 0 and i != 0:
            print("------------------------")
        for j in range (len(x[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
            if j == 8:
                print(x[i][j])
            else:
                print(str(x[i][j]) + " ", end = "")


# Finding the 0 on the board and returning it's xy coordinance
def find_empty(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == 0:
                return (i, j)
    return None
