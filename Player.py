
class Player:
    def __init__(self):
        self.userChar = {1: "X", -1: "O", 0: "_"}
        self.player_marker = ''
        self.bot_marker = ''
        self.player_name = ''
        self.bot_name = 'TBot'

    def get_marker(self):
        marker = input("Would you like your marker to be X or O?: ").upper()
        while marker not in ["X", "O"]:
            marker = input("Would you like your marker to be X  or O? :").upper()
        if marker == "X":
            # return ('X', 'Y')
            self.player_marker = 'X'
            self.bot_marker = 'O'
        else:
            self.player_marker = 'O'
            self.bot_marker = 'X'