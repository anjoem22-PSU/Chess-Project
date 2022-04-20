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

        self.piece_validators = {"p": self.pawn_move,
                                 "b": self.bishop_move,
                                 "r": self.rook_move,
                                 "k": self.king_move,
                                 "n": self.knight_move}

    # Checks if spaces between (x0,y0) and (x1,y1) are occupied
    def linear_open(self, p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]

        distance = 0
        x_step = 0
        y_step = 0

        if dx != 0:
            distance = dx - 1
            x_step = 1 if dx > 0 else -1

        if dy != 0:
            distance = dy - 1
            y_step = 1 if dy > 0 else -1

        print(distance)

        current_pos = [p1[0], p1[1]]
        for _ in range(abs(distance)):
            current_pos[0] += x_step
            current_pos[1] += y_step

            if self.__board[current_pos[1]][current_pos[0]] != "__":
                print("Something was in the way!")
                return False

        return True

    def pawn_move(self, p1, p2):
        p1_x, p2_x = p1[0], p2[0]
        p1_y, p2_y = p1[1], p2[1]

        color = self.__board[p1_y][p1_x][0]        
        direction = 1 if (color == "b") else -1
        pawn_rank = 1 if (color == "b") else 6
        can_boost = (p1_y == pawn_rank)

        dy = p2_y - p1_y
        dx = p2_x - p1_x
        
        if (dy != direction) and not (can_boost and dy == direction * 2):
            if can_boost:
                print("Pawn can only move up to two tiles forward")
            else:
                print("Pawn can only move one tile forward")
            return False

        if (dy == direction * 2) and dx != 0:
            print("Captures can't be made from two tiles away")
            return False

        p2_piece = self.__board[p2_y][p2_x]

        if dx == 0 and p2_piece != "__":
            print("Cannot capture with a forward move")
            return False
        
        if abs(dx) == 1 and (p2_piece == "__" or p2_piece[0] == color):
            if p2_piece == "__":
                print("Cannot move diagonally into an empty tile")
            else:
                print("You were blocked by your own piece")
            return False
        
        if abs(dx) > 1:
            print("Pawns cannot just slide around like a queen. Behave yourself!")
            return False

        return True


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
            if not self.linear_open(p1, p2):
                return False
            if self.__board[p2_y][p2_x] == "__" or self.__board[p2_y][p2_x][0] != self.__board[p1_y][p1_x][0]:
                return True
            else: return False
        else: return False

    def bishop_move(self, p1, p2):
        p1_x, p2_x = p1[0], p2[0]
        p1_y, p2_y = p1[1], p2[1]

        if not (abs(p2_y - p1_y) == abs(p2_x - p1_x)):
            return False
        if not self.linear_open(p1, p2):
            return False

        # check whether the p2 square is empty or if there's an opposite color piece
        if self.__board[p2_y][p2_x] == "__" or self.__board[p2_y][p2_x][0] != self.__board[p1_y][p1_x][0]:
            return True
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

    def validate_move(self, piece, position):
        if piece == position:
            print("There was no move made!")
            return False

        x1, y1 = piece[0], piece[1]
        x2, y2 = position[0], position[1]

        if x1 < 0 or x1 > 7 or x2 < 0 or x2 > 7:
            print("Out of Bounds")
            return False
        if y1 < 0 or y1 > 7 or y2 < 0 or y2 > 7:
            print("Out of Bounds")
            return False

        p_value = self.__board[y1][x1]
        if p_value == "__":
            print("Cannot move an empty tile")
            return False
        if (self.__white_turn and p_value[0] == "b") or (not self.__white_turn and p_value[0] == "w"):
            print("Cannot move opponent's piece")
            return False

        p_type = p_value[1]
        if not self.piece_validators[p_type](piece, position):
            return False

        return True

    def make_move(self, piece, position):
        if not self.validate_move(piece, position):
            return False

        temp = self.__board[piece[1]][piece[0]]
        self.__board[piece[1]][piece[0]] = "__"
        self.__board[position[1]][position[0]] = temp

        self.__white_turn = not self.__white_turn
        return True


    def __str__(self):
        ret_value = "\n   0  1  2  3  4  5  6  7\n"
        i = 0
        for row in self.__board:
            ret_value += str(i) + " "
            for element in row:
                ret_value += str(element) + " "
            i += 1
            ret_value += "\n"

        return ret_value