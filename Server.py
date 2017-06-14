import socket

from Game import Game
from Board import Board
from Validator import InputDataValidator


def Main():
    Validator = InputDataValidator()
    TicTacToe = Game()
    board = Board()
    host = "127.0.0.1"
    port = 5001

    mySocket = socket.socket()
    mySocket.bind((host, port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print("Connection from: " + str(addr))
    count_round = 1
    while True:
        data = conn.recv(1024).decode()
        # data = str(data).upper()
        # print("Received from User: " + str(data))
        if count_round == 1:
            data = TicTacToe.help() + str(TicTacToe.board.print_board())
            conn.send(data.encode())
            count_round = count_round + 1
        else:
            # what_validator_return = Validator.validate(data)
            if Validator.validate_if_number_is_int(data):
                TicTacToe.human_move(data)
                TicTacToe.bot_move()
                # data =  TicTacToe.enter_game_loop2('h', data)
                if TicTacToe.board.is_winner('X'):
                    data = 'X is winner \n'
                elif TicTacToe.board.is_winner('Y'):
                    data = 'Y i winner \n'
                elif TicTacToe.board.is_board_full():
                    data = 'Board is full.'
            else:
                 data = "This is not int. Type again."

            data = data + "\n" + str(TicTacToe.board.print_board())
            conn.send(data.encode())
            count_round = count_round + 1

    conn.close()


if __name__ == '__main__':
    Main()