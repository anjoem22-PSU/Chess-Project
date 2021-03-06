import board

# List of commands to automatically run for debugging
# DEBUG_LIST = [
#   "A2 A3",
#   "D7 D6",
#   "A1 A2",
#   "C8 E6",
#   "A2 A1",
#   "D8 D7",
#   "A1 A2",
#   "B8 A6",
#   "A2 A1"
# ]

def main():
    game = board.Board()
    l_dict = {
      "A" : 0,
      "B" : 1,
      "C" : 2,
      "D" : 3,
      "E" : 4,
      "F" : 5,
      "G" : 6,
      "H" : 7
    }
  
    continuing = True
    while continuing:
      print(game)

      # Comment out this code for debugging
      # user_input = "NONE"
      # if DEBUG_LIST:
      #   user_input = DEBUG_LIST.pop(0)
      # else:
      user_input = input("Enter your move here: ")
      
      if user_input == "STOP":
        continuing = False
        continue
      else:
        input_satisfied = False
        while not input_satisfied:
          p1,p2 = -1,-1
          try:
            coordinates = user_input.split()
            if len(coordinates) != 2:
              raise ValueError("Only Two Coordinates Expected")
            inp_a,inp_b = coordinates
            x1,x2 = l_dict[inp_a[0].upper()],l_dict[inp_b[0].upper()]
            y1,y2 = 8 - int(inp_a[1]), 8 - int(inp_b[1])
            p1 = (x1,y1)
            p2 = (x2,y2)
            input_satisfied = True
          except:
            user_input = input("Invalid input, try again!")
        game.attempt_move(p1, p2)
        message = game.get_message()
        print(message)
        if message == "Checkmate!" or message == "Stalemate!":
          print(game)
          user_input = input("Want to play again? (y/n)")
          if user_input.lower()[0] == "y":
            del game
            game = board.Board()
          else:
            print("Thanks for playing")
            continuing = False
          
      print()
        

if __name__ == '__main__':
    main()