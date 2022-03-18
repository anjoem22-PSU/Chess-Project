class Board:
    def __init__(self):
        self.__board = []
        for i in range(8):
            self.__board.append(["xx", "xx", "xx", "xx", "xx", "xx", "xx", "xx"])

    def __str__(self):
        ret_value = ""
        for row in self.__board:
            for element in row:
                ret_value += str(element) + " "
            ret_value += "\n"

        return ret_value
