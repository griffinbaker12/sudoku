board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def valid(b, num, pos):
    currI, currJ = pos

    for j in range(len(b[0])):
        if j == currJ:
            continue

        if num == b[currI][j]:
            return False

    for i in range(len(b)):
        if i == currI:
            continue

        if num == b[i][currJ]:
            return False

    box_x = (currI // 3) * 3
    box_y = (currJ // 3) * 3

    # (1,4) => 0, 3

    for i in range(0, 3):
        for j in range(0, 3):
            if b[i + box_x][j + box_y] == num:
                return False

    return True


def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")


def get_answer(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                for num in range(1, 10):
                    if valid(board, num, (i, j)):
                        board[i][j] = num
                        get_answer(b)
                        # somewhere along the way, you must have been wrong, so reset and go back through the numbers
                        board[i][j] = 0
                # if you have gone through the numbers for a certain square, and none of them worked, then go back to the call that called you
                return
    # you have tried all of the numbers (rum the above code on all of the objects on the board), so return the board
    print_board(b)


get_answer(board)

# print_board(board)
