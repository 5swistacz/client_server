import socket
import time
from Game import Game
from Board import Board


def Main():
    TicTacToe = Game()
    board = Board()
    host = "127.0.0.1"
    port = 5001

    mySocket = socket.socket()
    mySocket.bind((host, port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print("Connection from: " + str(addr))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            data = TicTacToe.help()
            conn.send(data.encode())
        print("from connected  user: " + str(data))

        data = str(data).upper()
        print("Received from User: " + str(data))

        data = TicTacToe.help() + str(board.print_board())
        conn.send(data.encode())


    conn.close()


if __name__ == '__main__':
    Main()