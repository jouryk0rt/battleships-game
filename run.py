# constants
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
SHOT_MISSED = "Shot has missed"
player_name = input("Please enter you name:")
# battleship coordinates
battleships = [[0, 1, 0, 1], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
total_hits = 0
total_turns = 0
print(BANNER)
while total_hits < 4:
    rows = 0
    columns = 0
    print(f"{player_name} Get ready to attack!")
    rows = int(input("Select a row to attack between 0 and 3:"))
    columns = int(input("Select a column to attack between 0 and 3:"))
    # calculate if hit or miss and total number of shots needed
    if battleships[rows][columns]:
        battleships[rows][columns] = 0
        total_hits += 1
        minus_hits = 4 - total_hits
        user_msg = "Hit :" + str(minus_hits) + " Hits left to win"
        print(user_msg)
   
    else:
        print(SHOT_MISSED)
    total_turns += 1
while False:
    try:
        print("Sorry I dont understand that")
    except IndexError():
        print("lol")
        continue
    else: 
        break
# Win Message
print("Win!")
win_text = f" {player_name} achieved victory in "
turns_text = " turns"
print(win_text + str(total_turns) + turns_text)
