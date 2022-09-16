from random import randint

# Board for holding ship locations
HOLDING_BOARD = [[" "] * 8 for x in range(8)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 8 for i in range(8)]
# Banner image which gets called later in the program
BANNER = """
 /$$$$$$$              /$$     /$$     /$$                           /$$       /$$          
| $$__  $$            | $$    | $$    | $$                          | $$      |__/          
| $$  \ $$  /$$$$$$  /$$$$$$ /$$$$$$  | $$  /$$$$$$         /$$$$$$$| $$$$$$$  /$$  /$$$$$$ 
| $$$$$$$  |____  $$|_  $$_/|_  $$_/  | $$ /$$__  $$       /$$_____/| $$__  $$| $$ /$$__  $$
| $$__  $$  /$$$$$$$  | $$    | $$    | $$| $$$$$$$$      |  $$$$$$ | $$  \ $$| $$| $$  \ $$
| $$  \ $$ /$$__  $$  | $$ /$$| $$ /$$| $$| $$_____/       \____  $$| $$  | $$| $$| $$  | $$
| $$$$$$$/|  $$$$$$$  |  $$$$/|  $$$$/| $$|  $$$$$$$       /$$$$$$$/| $$  | $$| $$| $$$$$$$/
|_______/  \_______/   \___/   \___/  |__/ \_______/      |_______/ |__/  |__/|__/| $$____/ 
                                                                                  | $$      
                                                                                  | $$      
                                                                                  |__/      
"""

# setting up board
def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


# ask name to make it more interactive and switching letters into numbers
player_name = input("Please enter you name:")
letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
print(BANNER)
# computer create 5 ships
def generate_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"


# Gameplay, selecting which row and which column needs to be attacked
def get_ship_location():
    row = input(f"{player_name}, Select a row to attack: ").upper()
    while row not in "12345678":
        print("Choice is not supported, valid row choices are 1,2,3,4,5,6,7 or 8")
        row = input("Select a row to attack: ").upper()
    column = input("Select a column to attack: ").upper()
    while column not in "ABCDEFGH":
        print("Choice is not supported, valid column choices are A,B,C,D,E,F,G or H")
        column = input("Select a column to attack: ").upper()
    return int(row) - 1, letters_to_numbers[column]


# check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


# Messages for choose location, hit, already guessed, win, etc
if __name__ == "__main__":
    generate_ships(HOLDING_BOARD)
    turns = 15
    while turns > 0:
        print("Choose location for attack, you need 2 hits to win")
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-":
            print(f"{player_name}, you have guessed that location previously.")
        elif HOLDING_BOARD[row][column] == "X":
            print("Hit!")
            GUESS_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("You have missed!")
            GUESS_BOARD[row][column] = "-"
            turns -= 1
        if count_hit_ships(GUESS_BOARD) == 2:
            print(f"Congratulations {player_name}, you  won!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You have no turns left")
