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

    # Checks if spaces between (x0,y0) and (x1,y1) are occupied
    # when diagonal_switch is false, the move must be cardinal (straight up/down/left/right)
    # otherwise the move must be diagonal
    def linear_open(self, p1, p2, diagonal_switch=False):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]

        if not diagonal_switch:
            if dx != 0 and dy != 0:
                print("A cardinal move was not made!")
                return False
        else:
            if not (dx == dy):
                print("A diagonal move was not made!")
                return False

        distance = 0
        x_step = 0
        y_step = 0

        if dx != 0:
            distance = dx - 1
            x_step = 1 if dx > 0 else -1

        if dy != 0:
            distance = dy - 1
            y_step = 1 if dy > 0 else -1

        current_pos = [p1[0], p1[1]]
        for _ in range(distance):
            current_pos[0] += x_step[0]
            current_pos[1] += y_step[1]
            if self.__board[current_pos[1]][current_pos[0]] != "__":
                # Something was in the way!
                return False
        return True

    def pawn_move(self, p1, p2):
        p1_x, p2_x = p1[0], p2[0]
        p1_y, p2_y = p1[1], p2[1]
        
        # validating moves for white pawn
        if self.__board[p1_y][p1_x] == "wp":
            # check whether the p2 square is empty
            if self.__board[p2_y][p2_x] != "__":
                # pawns can't move backwards
                if p2_y >= p1_y:
                    return False
                # if the pawn is on the 2nd row, moving two squares forward is valid
                elif p1_y == 6 and p2_y == p1_y - 2:
                    return True
            elif self.__board[p2_y][p2_x][0] == "b":
                if p2_y == p1_y-1 and (p2_x == p1_x-1 or p2_x == p1_x+1):
                    return True
                else: return False
            else: return False
        # validating moves for black pawns (follows the same logic as white)
        if self.__board[p1_y][p1_x] == "bp":
            # check whether the p2 square is empty
            if self.__board[p2_y][p2_x] != "__":
                # pawns can't move backwards
                if p2_y <= p1_y:
                    return False
                # if the pawn is on the 6th row, moving two squares forward is valid
                elif p1_y == 1 and p2_y == p1_y + 2:
                    return True
            # if there's a white piece on any of the forward diagonal squares, the pawn should be able to capture it
            elif self.__board[p2_y][p2_x][0] == "w":
                if p2_y == p1_y+1 and (p2_x == p1_x-1 or p2_x == p1_x+1):
                    return True
                else: return False
            else: return False

    def queen_move(self, p1, p2):
        # queen can move like a bishop or a rook
        if self.bishop_move(p1, p2) or self.rook_move(p1, p2):
            return True
        else: return False

    def king_move(self, p1, p2):
        p1_x, p2_x = p1[0], p2[0]
        p1_y, p2_y = p1[1], p2[1]
        #check whether the p2 square is empty or if there's an opposite color piece
        if self.__board[p2_y][p2_x] == "__" or self.__board[p2_y][p2_x][0] != self.__board[p1_y][p1_x][0]:
            # the king can move 1 square in any direction
            if abs(p2_y - p1_y) == 1 or abs(p2_x - p1_x) == 1:
                return True
            else: return False
        else: return False

    def rook_move(self, p1, p2):
        p1_x, p2_x = p1[0], p2[0]
        p1_y, p2_y = p1[1], p2[1]
        # rook can move vertically or horizontally
        if p2_x == p1_x or p2_y == p1_y:
            if self.___board[p2_y][p2_x] == "__" or self.__board[p2_y][p2_x][0] != self.__board[p1_y][p1_x][0]:
                return True
            else: return False
        else: return False

    def bishop_move(self, p1, p2):
        p1_x, p2_x = p1[0], p2[0]
        p1_y, p2_y = p1[1], p2[1]
        # check whether the p2 square is empty or if there's an opposite color piece
        if self.__board[p2_y][p2_x] == "__" or self.__board[p2_y][p2_x][0] != self.__board[p1_y][p1_x][0]:
            # bishop can move in a diagonal
            if abs(p2_y-p1_y) == abs(p2_x-p1_x):
                return True
            else: return False
        else: return False

    def knight_move(self, p1, p2):
        p1_x, p2_x = p1[0], p2[0]
        p1_y, p2_y = p1[1], p2[1]
        # check whether the p2 square is empty or if there's an opposite color piece
        if self.__board[p2_y][p2_x] == "__" or self.__board[p2_y][p2_x][0] != self.__board[p1_y][p1_x][0]:
            if abs(p2_y - p1_y) == 2 and abs(p2_x-p1_x) == 1:
                return True
            elif abs(p2_y-p1_y) == 1 and abs(p2_x-p1_x) == 2:
                return True
        else: return False

    def attempt_move(self, piece, position):
        if piece == position:
            print("There was no move made!")
            return False

        x1, y1 = piece[0], piece[1]
        x2, y2 = position[0], position[1]

        p_value = self.__board[y1][x1]
        if p_value == "__":
            print("Cannot move an empty tile")
            return False
        if (self.__white_turn and p_value[0] == "b") or (not self.__white_turn and p_value[0] == "w"):
            print("Cannot move opponent's piece")
            return False

    def __str__(self):
        ret_value = ""
        for row in self.__board:
            for element in row:
                ret_value += str(element) + " "
            ret_value += "\n"

        return ret_value
