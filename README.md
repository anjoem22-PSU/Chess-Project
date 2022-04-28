# Chess-Project
Some kind of chess program

__Summary__
This is a (currently) terminal based chess program. Just run main.py and it should just work. This does not require any packages whatsoever.
The board is shown as an eight by eight grid with a pair of characters representing a piece. An empty tile is represented by two underscores.
The first character of a tile dictates the color (w = White, b = Black)
The second character is the piece type (p = Pawn, n = kNight, k = King, r = Rook, b = Bishop, q = Queen)

While this isn't particularly pretty or efficient, it should be fully functional including en passant and castling.
To castle, type a move that would move the king to the rook's position. The rook you pick determines which side your king castles to.

__Controls__
To make a move, type two pairs of characters seperated by a space.
The first character of each pair represents an x value and ranges from A-H as indicated by the board printout
The second character is a y value and ranges from 1-8 as is indicated by the board printout.

__How to Play?__
You are waging an epic war against an opposing nation due to the color they attached to their army. 
The goal is to capture their king, though you cannot do so directly. You must put your opponent in a position that any possible move 
they make would lead to the loss of their king. If the opponent can take your king on the next move, you must bring it to safety,
either through moving the king, blocking the attack with another piece, or capturing the offensive piece.

PAWNS:
  Pawns may move one tile forward each turn. If they have not moved yet, they may move two tiles forward.
  Pawns cannot move forward if there is a piece in the way. If there is a piece one space diagonally forward to the pawn, it may be brutally murdered.
  If a pawn moves two tiles forward, an opposing pawn can capture it as though it had only moved forward one tile (only on the next turn).
  Pawns that reach the edge of the board are promoted to a queen. (In standard chess you can choose, but screw you queen only)
  
ROOKS:
  Rooks can move an unlimited number of spaces, but only in cardinal directions (up/down/left/right). 
  They may not jump over pieces, but can obliterate a troop by ramming in them at sonic speeds
  
BISHOPS:
  Bishops can move an unlimited number of spaces, but only diagonally.
  They may not jump over pieces, but can violently exterminate a foe by stabbing their blades through the heart of a troop.
  NOTE: While there are two bishops, there is a "black square" and "white square" bishop. There is no move that puts these two on the same tile.
  
QUEENS:
  A queen is a bishop and a rook conjoined together through some horrific frankenstein-like process.
  This piece is the most capable of committing violent acts of murder, thus making it one of the most important pieces
  
KING:
  A king can move in any direction, but only one space away.
  If an opponents piece can capture the king (CHECK), the king must be brought to safety.
  If no move can bring it to safety, the opponent wins (CHECKMATE).
  If the king is not threatened, but every possible move would put it in danger, the game ends in a draw (STALEMATE)
  
KNIGHT:
  A night can move two tiles in one direction and then one in another direction (like an L shape).
  This is the only piece that can hop over other pieces.

Rules for castling:
  1. The king may not be moved prior to castling. The rook on the side where the king will castle also cannot be moved.
  2. There must not be any tiles between the king and the rook on the side being castled
  3. Castling may not occur when the king is in check or if the king would be in check when inbetween the rook and empty tiles
With these conditions satisfied, the king will move two spaces in the castle direction and the rook will be placed next to the king opposite to the side castled


I haven't really play tested this yet, so it may burn up and explode. Hopefully that isn't the case.
