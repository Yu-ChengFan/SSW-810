board = [
    [0,3,0,0,0,0,0,0,1],
    [9,0,7,0,8,0,0,3,0],
    [0,8,0,2,0,4,6,0,0],
    [4,0,0,6,0,7,3,1,0],
    [8,7,0,0,2,0,0,0,9],
    [0,0,3,1,0,0,0,4,2],
    [0,1,0,0,0,0,0,8,0],
    [5,0,2,0,6,0,0,7,0],
    [0,0,0,3,0,5,4,0,6]
]



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
                
def find_empty(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == 0:
                return (i, j)
            
print(print_board(board))