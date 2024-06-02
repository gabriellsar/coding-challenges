from p5 import *

game = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

players = ['X', 'O']
current_player = 0

TAM = 600


def draw_board(board):
    # board
    line(200, 0, 200, TAM)
    line(400, 0, 400, TAM)
    line(0, 200, TAM, 200)
    line(0, 400, TAM, 400)

    # text section
    quad(0, TAM, TAM, TAM, TAM, TAM + 100, 0, TAM + 100)

    for y, lines in enumerate(board):
        for x, space in enumerate(lines):
            cof_x, cof_y = (200 * x), (200 * y)
            if space == "X":
                line(50 + cof_x, 50 + cof_y, 150 + cof_x, 150 + cof_y)
                line(50 + cof_x, 150 + cof_y, 150 + cof_x, 50 + cof_y)

            elif space == "O":
                circle(100 + cof_x, 100 + cof_y, 100)


def valid_move(board, x, y) -> bool:
    if board[y][x] == '':
        return True
    return False


def run_coop_game(board, p_markers, current_p) -> str:
    global current_player
    if mouse_is_pressed and valid_move(board, find_grid_position(mouse_x), find_grid_position(mouse_y)):
        place_marker_player(board, p_markers[current_p])
        current_player += 1
    return win_check(board)


def run_game() -> str:
    s = run_coop_game(game, players, current_player % 2)
    draw_board(game)
    return s


def win_check(board) -> str:
    for y, _ in enumerate(board):
        if board[y][0] == board[y][1] == board[y][2] and board[y][0] != '':
            return players[(current_player % 2) - 1]
        for x, __ in enumerate(_):
            if board[0][x] == board[1][x] == board[2][x] and board[0][x] != '':
                return players[(current_player % 2) - 1]

    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != '':
        return players[(current_player % 2) - 1]
    elif board[2][0] == board[1][1] == board[0][2] and board[1][1] != '':
        return players[(current_player % 2) - 1]

    if current_player >= 9:
        return "tie"
    return "em jogo"


def find_grid_position(value):
    return int(value // 200)


def place_marker_player(board, marker):
    position_x = find_grid_position(mouse_x)
    position_y = find_grid_position(mouse_y)
    board[position_y][position_x] = marker
    return board


# p5 base functions

def setup():
    size(TAM, TAM + 100)
    stroke(255)
    strokeWeight(4)
    noFill()


def draw():
    background(0)
    result = run_game()
    if result == "tie":
        noLoop()
        text("O jogo empatou", 10, TAM + 50)
    elif result == players[(current_player % 2) - 1]:
        noLoop()
        text(f"O jogador {result} ganhou o jogo", 10, TAM + 50)


if __name__ == '__main__':
    run()
