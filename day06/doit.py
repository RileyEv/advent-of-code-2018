# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from typing import List, Tuple

def readfile() -> List[Tuple[int,int]]:
    contents: List[Tuple[int,int]] = []
    with open('input.txt', 'r') as f:
        for line in f:
            split_line: List[str] = line.split(', ')
            contents.append((int(split_line[0]), int(split_line[1])))
    return contents


def get_max_coordinates(coordinates: List[Tuple[int,int]]) -> Tuple[int,int]:
    return (
        max(coordinates, key=lambda a: a[0])[0],
        max(coordinates, key=lambda a: a[1])[1]
    )

def create_board(contents: List[Tuple[int,int]], empty_cell_val: int=100000) -> List[List[Tuple[int,int]]]:
    max_coordinates = get_max_coordinates(contents)
    board = [
        [
            (0,empty_cell_val) for x in range(max_coordinates[0] + 2)
        ] for y in range(max_coordinates[1] + 2)
    ]
    for i, coordinate in enumerate(contents, 1):
        board[coordinate[1]][coordinate[0]] = (i, 0)
    return board

def get_dist(cell1: Tuple[int,int], cell2: Tuple[int,int]) -> int:
    return abs(cell1[0]-cell2[0]) + abs(cell1[1] - cell2[1])


def process_round(
        i: int,
        coor: Tuple[int,int],
        board: List[List[Tuple[int,int]]]
) -> List[List[Tuple[int,int]]]:
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            distance = get_dist((x,y), coor)
            if board[y][x][1] == distance and board[y][x][0] != i:
                board[y][x] = (0, distance)
            elif board[y][x][1] > distance:
                board[y][x] = (i, distance)
    return board

def get_non_infinite_coors(board: List[List[Tuple[int,int]]], n: int) -> List[int]:
    non_infinite = list(range(1, n + 1))
    for i in range(len(board[0])):
        try:
            non_infinite.remove(board[0][i][0])
        except ValueError:
            pass
        try:
            non_infinite.remove(board[-1][i][0])
        except ValueError:
            pass

    for i in range(len(board)):
        try:
            non_infinite.remove(board[i][0][0])
        except ValueError:
            pass
        try:
            non_infinite.remove(board[i][-1][0])
        except ValueError:
            pass

    return non_infinite

def get_count(board: List[List[Tuple[int,int]]], n: int) -> int:
    count: int = 0
    for row in board:
        for cell in row:
            if cell[0] == n:
                count += 1
    return count

def process_task2(board: List[List[Tuple[int,int]]], coor: Tuple[int,int]) -> List[List[Tuple[int,int]]]:
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            board[y][x] = (board[y][x][0], board[y][x][1] + get_dist((x, y), coor))
    return board

def count_area(board: List[List[Tuple[int,int]]]) -> int:
    count = 0
    for row in board:
        for cell in row:
            if cell[1] < 10000:
                count += 1
    return count

def main() -> None:
    file_contents = readfile()
    board = create_board(file_contents)
    for i, coor in enumerate(file_contents, 1):
        board = process_round(i, coor, board)

    non_infinite = get_non_infinite_coors(board, len(file_contents))

    largest_area: int = 0
    for coord in non_infinite:
        count = get_count(board, coord)
        if count > largest_area:
            largest_area = count
    print (largest_area)


    ## task 2
    board2 = create_board(file_contents, 0)
    for coor in file_contents:
        board2 = process_task2(board2, coor)

    print(count_area(board2))





    #for row in board:
    #    print(row)







if __name__ == '__main__':
    main()
