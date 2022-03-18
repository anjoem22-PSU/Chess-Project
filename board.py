class Board:
    def __init__(self):
        self.__board = []
        self.__white_turn = True

        for i in range(8):
            self.__board.append(["__", "__", "__", "__", "__", "__", "__", "__"])

        # Creates the pawns
        for i in range(8):
            self.__board[1][i] = "bp"

        for i in range(8):
            self.__board[6][i] = "wp"

        # Fill the rest of the pieces
        b_row = self.__board[0]
        b_row[0] = "br"
        b_row[1] = "bn"
        b_row[2] = "bb"
        b_row[3] = "bq"
        b_row[4] = "bk"
        b_row[5] = "bb"
        b_row[6] = "bn"
        b_row[7] = "br"

        w_row = self.__board[7]
        w_row[0] = "wr"
        w_row[1] = "wn"
        w_row[2] = "wb"
        w_row[3] = "wq"
        w_row[4] = "wk"
        w_row[5] = "wb"
        w_row[6] = "wn"
        w_row[7] = "wr"

    def pawn_move(self, p1, p2):
        pass

    def queen_move(self, p1, p2):
        pass

    def king_move(self, p1, p2):
        pass

    def rook_move(self, p1, p2):
        pass

    def bishop_move(self, p1, p2):
        pass

    def knight_move(self, p1, p2):
        pass

    def attempt_move(self, piece, position):
        x1, y1 = piece[0], piece[1]
        x2, y2 = position[0], position[1]

        p_value = self.__board[y1][x1]
        if p_value == "__":
            return False
        if (self.__white_turn and p_value[0] == "b") or (not self.__white_turn and p_value[0] == "w"):
            return False

    def __str__(self):
        ret_value = ""
        for row in self.__board:
            for element in row:
                ret_value += str(element) + " "
            ret_value += "\n"

        return ret_value
