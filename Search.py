def search_right_or_left(grid, r, c, piece):
    """
    * Takes in a grid and searches for Connect 4 WIN condition in left_to_right direction.
    :param grid: The board
    :param r: Row
    :param c: Column
    :param piece: Player 1 or Player 2
    :return: True or False
    """
    count = 0
    for i in range(1, 4):  # Check for piece in left direction
        if 0 <= c - i < 7:  # 0,7 ==> column limits
            if grid[r][c - i] == piece:
                count += 1
            else:
                break

    for j in range(1, 4):  # Check for piece in right direction
        if 0 <= c + j < 7:  # 0,7 ==> column limits
            if grid[r][c + j] == piece:
                count += 1
            else:
                break
    return count >= 3


def search_up_or_down(grid, r, c, piece):
    """
    * Takes a grid and searches for Connect 4 WIN condition in Up_to_Down Direction.
    :param grid: The board
    :param r: Row
    :param c: Column
    :param piece: Player 1 or Player 2
    :return: True or False
    """
    count = 0
    for i in range(1, 4):  # Check for piece in up direction
        if 0 <= r - i < 6:  # 0, 6 ==> row limits
            if grid[r - i][c] == piece:
                count += 1
            else:
                break

    for j in range(1, 4):  # Check for piece in down direction
        if 0 <= r + j < 6:  # 0, 6 ==> row limits
            if grid[r + j][c] == piece:
                count += 1
            else:
                break
    return count >= 3


def search_right_diagonal(grid, r, c, piece):
    """
    * Takes a grid and searches for Connect 4 WIN condition in top left_to_bottom right Direction
    :param grid: The board
    :param r: Row
    :param c: Column
    :param piece: Player 1 or Player 2
    :return: True or False
    """
    count = 0
    for i in range(1, 4):  # Check for piece in up-right direction
        if 0 <= c + i < 7 and 0 <= r - i < 6:  # 0,7 ==> column limits ; 0,6 ==> row limits
            if grid[r - i][c + i] == piece:
                count += 1
            else:
                break

    for j in range(1, 4):  # Check for piece in down-left direction
        if 0 <= c - j < 7 and 0 <= r + j < 6:  # 0,7 ==> column limits ; 0,6 ==> row limits
            if grid[r + j][c - j] == piece:
                count += 1
            else:
                break
    return count >= 3


def search_left_diagonal(grid, r, c, piece):
    """
    * Searches a grid for Connect 4 WIN condition in bottom_left TO top_right direction
    :param grid: The board
    :param r: Row
    :param c: Column
    :param piece: Player 1 or Player 2
    :return: True or False
    """
    count = 0
    for i in range(1, 4):  # Check for piece in up-left direction
        if 0 <= c - i < 7 and 0 <= r - i < 6:  # 0,7 ==> column limits ; 0,6 ==> row limits
            if grid[r - i][c - i] == piece:
                count += 1
            else:
                break

    for j in range(1, 4):  # Check for piece in down-right direction
        if 0 <= c + j < 7 and 0 <= r + j < 6:  # 0,7 ==> column limits ; 0,6 ==> row limits
            if grid[r + j][c + j] == piece:
                count += 1
            else:
                break
    return count >= 3
