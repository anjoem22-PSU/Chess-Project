class Board:
    def __init__(self):
        self.__board = []
        self.__white_turn = True
        self.__finished = False
        self.__message = "Game Started!"
      
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
                                 "n": self.knight_move,
                                 "q": self.queen_move}

    # Checks if spaces between (x0,y0) and (x1,y1) are occupied
    def linear_open(self, p1, p2):
      dx = p2[0] - p1[0]
      dy = p2[1] - p1[1]

      # Distance is how long the line is, x_step and y_step determine direction
      distance = 0
      x_step, y_step = 0, 0

      if dx != 0:
        distance = dx - 1
        x_step = 1 if dx > 0 else -1

      if dy != 0:
        distance = dy - 1
        y_step = 1 if dy > 0 else -1

      current_pos = [p1[0], p1[1]]
      for _ in range(abs(distance)):
        current_pos[0] += x_step
        current_pos[1] += y_step

        if self.__board[current_pos[1]][current_pos[0]] != "__":
          self.__message = "Something was in the way"
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
          self.__message = "This pawn can only move two units forward"
        else: 
          self.__message = "This pawn can only move one unit forward"
        return False

      if dy == direction * 2:
        if dx != 0:
          self.__message = "You cannot capture two tiles away"
          return False
        if self.__board[p2_y - direction][p2_x] != "__":
          self.__message = "You cannot hop over a piece"
          return False

      p2_piece = self.__board[p2_y][p2_x]

      if dx == 0 and p2_piece != "__":
        self.__message = "You cannot cardinally capture a piece with a pawn"
        return False
      
      if abs(dx) == 1 and (p2_piece == "__" or p2_piece[0] == color):
        self.__message = "Either you tried to capture an empty tile or your own team's pawn"
        return False
      
      if abs(dx) > 1:
        self.__message = "STOP TRYING TO SLIDE AROUND LIKE A LUNATIC!!!"
        return False

      return True

    def queen_move(self, p1, p2):
        # queen can move like a bishop or a rook
        if self.bishop_move(p1, p2) or self.rook_move(p1, p2):
            return True
        else: 
          return False

    def king_move(self, p1, p2):
      p1_x, p2_x = p1[0], p2[0]
      p1_y, p2_y = p1[1], p2[1]
      #check whether the p2 square is empty or if there's an opposite color piece
      if self.__board[p2_y][p2_x] == "__" or self.__board[p2_y][p2_x][0] != self.__board[p1_y][p1_x][0]:
          # the king can move 1 square in any direction
          if abs(p2_y - p1_y) > 1 or abs(p2_x - p1_x) > 1:
            return False
            self.__message = "The king can only move one unit in any direction"
          else: 
            return True
      else: 
        self.__message = "You cannot capture your own pieces"
        return False

    def rook_move(self, p1, p2):
      p1_x, p2_x = p1[0], p2[0]
      p1_y, p2_y = p1[1], p2[1]
      # rook can move vertically or horizontally
      if p2_x == p1_x or p2_y == p1_y:
        if not self.linear_open(p1, p2):
          return False
        if self.__board[p2_y][p2_x] == "__" or self.__board[p2_y][p2_x][0] != self.__board[p1_y][p1_x][0]:
          return True
        else: 
          self.__message = "Cannot capture your own pieces"
          return False
      else: 
        self.__message = "The rook can only move in cardinal directions"
        return False

    def bishop_move(self, p1, p2):
      p1_x, p2_x = p1[0], p2[0]
      p1_y, p2_y = p1[1], p2[1]

      if not (abs(p2_y - p1_y) == abs(p2_x - p1_x)):
        self.__message = "The bishop must move diagonally"
        return False
      if not self.linear_open(p1, p2):
        return False

      # check whether the p2 square is empty or if there's an opposite color piece
      if self.__board[p2_y][p2_x] == "__" or self.__board[p2_y][p2_x][0] != self.__board[p1_y][p1_x][0]:
        return True
      else: 
        self.__message = "Cannot capture your own pieces"
        return False

    def knight_move(self, p1, p2):
        p1_x, p2_x = p1[0], p2[0]
        p1_y, p2_y = p1[1], p2[1]
        # check whether the p2 square is empty or if there's an opposite color piece
        if self.__board[p2_y][p2_x] == "__" or self.__board[p2_y][p2_x][0] != self.__board[p1_y][p1_x][0]:
          if abs(p2_y - p1_y) == 2 and abs(p2_x-p1_x) == 1:
            return True
          elif abs(p2_y-p1_y) == 1 and abs(p2_x-p1_x) == 2:
            return True
          else:
            self.__message = "Not a valid horse move"
            return False
        else: 
          self.__message = "Cannot capture your own pieces"
          return False

    # This swaps two pieces and returns a list of edited pieces with their previous state
    def swap_pieces(self,p1,p2):
      old_states = []
      x1, y1 = p1[0], p1[1]
      x2, y2 = p2[0], p2[1]

      piece1 = self.__board[y1][x1]
      piece2 = self.__board[y2][x2]
      self.__board[y1][x1] = "__"
      self.__board[y2][x2] = piece1

      if piece1[1] == "p" and (y2 == 0 or y2 == 7):
        self.__board[y2][x2] = piece1[0] + "q"

      old_states.append((p1,piece1))
      old_states.append((p2,piece2))
      return old_states
          
    # Determine if this move causes the king to be in check
    # This is a brute force method, and so it surely isn't efficient. Oh well
    def test_check(self, p1, p2):
      check_found = False
      old_states = self.swap_pieces(p1,p2)
    
      # Find King
      kx, ky = -1, -1
      for y, row in enumerate(self.__board):
          if kx != -1 and ky != -1:
              break
          for x, piece in enumerate(row):
              if piece[1] == "k" and piece[0] == ("w" if self.__white_turn else "b"):
                  kx = x
                  ky = y
                  break

      # See if any piece can capture the king
      self.__white_turn = not self.__white_turn
      for y, row in enumerate(self.__board):
          if check_found:
              break
          for x, piece in enumerate(row):
            if self.validate_move((x, y), (kx, ky)):
                check_found = True
                break
      self.__white_turn = not self.__white_turn
      
      for state in old_states:
        position = state[0]
        piece = state[1]
        self.__board[position[1]][position[0]] = piece
        
      return check_found

    def validate_move(self, piece, position):
      if piece == position:
        self.__message = "No move was made"
        return False

      x1, y1 = piece[0], piece[1]
      x2, y2 = position[0], position[1]

      if x1 < 0 or x1 > 7 or x2 < 0 or x2 > 7:
        self.__message = "Input out of bounds"
        return False
      if y1 < 0 or y1 > 7 or y2 < 0 or y2 > 7:
        self.__message = "Input out of bounds"
        return False

      p_value = self.__board[y1][x1]
      if p_value == "__":
        self.__message = "No piece was selected"
        return False
      if (self.__white_turn and p_value[0] == "b") or (not self.__white_turn and p_value[0] == "w"):
        self.__message = "That pieces is not yours!"
        return False

      p_type = p_value[1]
      if not self.piece_validators[p_type](piece, position):
          return False

      #Determine if king is in check
      if self.test_check(piece, position):
        self.__message = "This move leaves the king in check!"
        return False

      return True

    def attempt_move(self, piece, position):
        if not self.validate_move(piece, position):
          return False

        # Actually move pieces, change to the other player's turn
        self.swap_pieces(piece,position)
        self.__white_turn = not self.__white_turn
        self.__message = "Move successful"
        return True

    def __str__(self):
        ret_value = ""
        i = 0
        for row in self.__board:
            ret_value += str(8 - i) + " "
            for element in row:
                ret_value += str(element) + " "
            i += 1
            ret_value += "\n"

        ret_value += "  A  B  C  D  E  F  G  H \n"
        return ret_value

    def get_message(self):
      return self.__message
