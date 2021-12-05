from utils import get_input_file, inputfile_to_array

get_input_file(4)

input_list = inputfile_to_array("inputs/input_day_4.txt")

bingo_numbers = input_list.pop(0).split(",")
input_list.pop(0) # Removing first empty string between numbers and boards

def make_bingo_cards(board_list):
    bingo_boards = []
    single_board = []
    for element in board_list:
        if element == "":
            bingo_boards.append(single_board)
            single_board = []
        else:
            row = element.split()
            single_board.append(row)
    return bingo_boards

def make_marker_boards(bingo_boards, board_size=5):
    marker_boards = []
    for i in bingo_boards:
        marker_board = [[0 for x in range(board_size)] for y in range(board_size)]
        marker_boards.append(marker_board)
    return marker_boards

def mark_board(number, bingo_board, marker_board):
    for row_number, row in enumerate(bingo_board):
        for col_number, number_at_placement in enumerate(row):
            if number == number_at_placement:
                marker_board[row_number][col_number] = "X"
    return marker_board

def get_score(bingo_board, marker_board, last_called_number):
    score = 0
    for row_number, row in enumerate(bingo_board):
        for col_number, number_at_placement in enumerate(row):
            if marker_board[row_number][col_number] != "X":
                score += int(bingo_board[row_number][col_number])
    score = int(last_called_number) * score
    return score


def is_bingo(marker_board):
    column_checker = [1] * len(marker_board[0]) # column has bingo until proven otherwise
    for row_number, row in enumerate(marker_board):
        if 0 not in row:
            return True
        for col_number, element_at_placement in enumerate(row):
            if element_at_placement == 0: # Not bingo in that column
                column_checker[col_number] = 0 # marks that column as "not bingo"
    if 1 in column_checker:
        return True
    return False

def get_first_winning_score(bingo_numbers, bingo_boards):
    marker_boards = make_marker_boards(bingo_boards)
    for bingo_number in bingo_numbers:
        for board_number, bingo_board in enumerate(bingo_boards):
            marker_board = marker_boards[board_number]
            mark_board(bingo_number, bingo_board, marker_board)
            if is_bingo(marker_board):
                return get_score(bingo_board, marker_board, bingo_number)
    print("No winner?")

def get_last_winning_score(bingo_numbers, bingo_boards):
    winning_boards = [0]*len(bingo_boards)
    marker_boards = make_marker_boards(bingo_boards)
    for bingo_number in bingo_numbers:
        for board_number, bingo_board in enumerate(bingo_boards):
            marker_board = marker_boards[board_number]
            mark_board(bingo_number, bingo_board, marker_board)
            if is_bingo(marker_board) and not winning_boards[board_number]:
                last_winning_board = bingo_board
                last_winning_marker_board = marker_board
                last_winning_bingo_number = bingo_number
                winning_boards[board_number] = 1
                last_score = get_score(
                    last_winning_board,
                    last_winning_marker_board,
                    last_winning_bingo_number)
    return last_score


bingo_boards = make_bingo_cards(input_list)

print ("First answer: ", get_first_winning_score(bingo_numbers, bingo_boards))
print ("Second answer: ", get_last_winning_score(bingo_numbers, bingo_boards))
