import pygame
import board

def main():
    game = board.Board()

    continuing = True
    while continuing:
        print(game)
        user_input = input("Enter your move here")
        if user_input == "STOP":
            continuing = False
            continue
        else:
            p1, p2 = user_input.split()
            p1 = (int(p1[0]), int(p1[1]))
            p2 = (int(p2[0]), int(p2[1]))
            success = game.make_move(p1, p2)
            print(success)

        print()





if __name__ == '__main__':
    main()

