# Individual Project
# HDDS1101 Introduction to Computing and Programming
# Student ID: 22661026
# Name: Herman, To Ho Hin
# Minesweeper
import random

# Constants of the game
NUM_COLUMN = 4
NUM_ROW = 4
NUM_MINE = 5 # fixed mine number NUM_COLUMN * NUM_ROW

#   symbols of the game board
#   ' ': not revealed
SYMBOL_NORMAL = ' '
#   '*': mine
SYMBOL_MINE = '*'
#   '!': flag
SYMBOL_FLAG = '!'
#   '0' to '8': no. of mines in the surrounding
SYMBOL_TICK = '√'  # used squre root symbol for tick, can use Unicode too (u'\u2713' = '✓')
SYMBOL_CROSS = 'x' # used x for cross, or possibly Unicode (u'\u2715' # ✕	U+2715)


# underlying mines
mine_list = []
# game board
game_board = []



# draw mine list
def draw_mine_list():
    mine_list.clear()
    for i in range(NUM_MINE):
        # need briefing about chr() function
        invalid_choice = True
        while (invalid_choice):
            column = random.randrange(1, NUM_COLUMN+1)
            row = random.randrange(1,NUM_ROW+1)
            if ((row,column) in mine_list):
                invalid_choice = True
            else:
                invalid_choice = False
        # make sure no repeat
        mine_list.append((row, column))

#reset game board
def reset_game_board():
    game_board.clear
    for r in range(NUM_ROW+2):
        row_list = []
        for c in range(NUM_COLUMN+2):
            row_list.append(SYMBOL_NORMAL)
        game_board.append(row_list)

def display_game_board():
    print("  ", end='')
    for c in range(1, NUM_COLUMN+1):
       print(f" {c}", end='')
    print() #end line
    print("  -", "--" * NUM_COLUMN, sep='')
    for r in range(1,NUM_ROW+1):
        print(f"{r} |", end='')
        for c in range(1,NUM_COLUMN+1):
            print(game_board[r][c], sep="", end="|")
        print("") # print end line
    print("  -", "--" * NUM_COLUMN, sep='')


# is_mine_position(row,col)
def is_mine_position(row,col):
    t = (row, col)
    for mine in mine_list:
        if mine == t:
            # the choice is a mine.
            return True
    return False

def check_mine(r,c):
    n_M = 0
    for x in range (r-1,r+2):
        for y in range(c-1,c+2):
            if is_mine_position(x,y):
                n_M += 1 
    return n_M 

# row -1 col -1 check 
# main game
def main_game():
    # set var
    heart = 3
    mine = 5 
    flag = 5
    round = 0
    row = 0
    col = 0
    playerName = ()
    command = ()
    draw_mine_list()
    reset_game_board()
    print("----------------------------------")
    print("|Welcome to the SCE Minesweeper~!|")
    print("----------------------------------")
    playerName = str(input("Please input your name:"))
    print(f"Welcome, {playerName}")
    while heart != 0 and mine  != 0  and flag !=0 and command != "q" :
        round += 1  
        print(f"Round {round},")
        print(f"Hidden mines: {mine};{playerName}, you have {heart} hearts and {flag} flags.")
        display_game_board()
        print (mine_list)
        print("Commands: c=clear mine, m=mark mine, i=introduction, q=quit")
        command = str(input(f"{playerName}, pleaese input your next action: "))
        # clear mine
        if command == "c":
            row = int(input("Input row to mark: "))
            col = int(input("Input column to mark: "))
            while  row > 4 or col > 4 or row < 1 or col < 1: 
                print("Invalid row or column choice")
                row = int(input("Input row to mark: "))
                col = int(input("Input column to mark: "))
            if game_board == SYMBOL_FLAG:
                game_board[row][col] = SYMBOL_NORMAL
                flag += 1 
                game_board[row][col] = check_mine(row,col)
                print(f"For ({row},{col}), there are {game_board[row][col]} mine(s) in the surrounding cells")
            if is_mine_position(row,col):
                print(f"You steppted in the mine at ({row},{col})")
                heart -= 1
                game_board[row][col] = SYMBOL_MINE
                mine -= 1 
            else:
                game_board[row][col] = check_mine(row,col)
            # mark mine 
        elif command == "m":
            row = int(input("Input row to mark: "))
            col = int(input("Input column to mark: "))
            while  row > 4 or col > 4 or row < 1 or col < 1: 
                print("Invalid row or column choice")
                row = int(input("Input row to mark: "))
                col = int(input("Input column to mark: "))
            if game_board[row][col] == SYMBOL_NORMAL:
                print(f"You marked ({row},{col}) as '!'. ")
                flag -= 1 
                game_board[row][col] = SYMBOL_FLAG
                if game_board[row][col] != SYMBOL_NORMAL:
                    print(f"Cell ({row},{col}) is already revealed or marked. ")
        # introduction
        elif command == "i":
            print("You will have 3 hearts to find mine in the mine sweeper.")
            print("And you will have 5 flags to mark the mine field. ")
            print("You can choose the location by input the coordination in the mine field.")
            print("Clear mine (c): The player will choose a cell to clear the mine.")
            print("Mark mine (m): The player will mark a cell as a hidden mine with flag symbol '!'")
            print("Introduction (i): This command will show a short introduction of the game, and the author's name")
            print("Quit (q): This command exits the game. The resulting game board will be marked and shown.")
            print("To achieve the victory, You need to have 1 heart at least and make movements.")
            print("Full name of the programmer: To Ho Hin, Herman")
        # quit game
        elif command == "q":
            print(f"Goodbye, {playerName}")
            break
            
        else:
            print("Invalid choice, please input either 'c', 'm', 'i' or 'q'.")
            command = str(input(f"{playerName}, pleaese input your next action: "))
    # get the result of the game
    for row in range(1,5):
        for col in range(1,5):
            if game_board[row][col] == SYMBOL_FLAG and (row,col) in mine_list:
                game_board[row][col] = SYMBOL_TICK
            elif  game_board[row][col] == SYMBOL_FLAG and (row,col) not in mine_list:
                game_board[row][col] = SYMBOL_CROSS
                heart -= 1 
                if heart < 0:
                    heart = 0
    # reveal the end game board
    for x,y in mine_list:
        if game_board[x][y] == SYMBOL_NORMAL:
            game_board[x][y] = SYMBOL_MINE
            heart -= 1 
            if heart < 0 :
                heart = 0
    # game over
    print("Game is over.")
    print("The resulting game board is: ")
    print(f"Hidden mines 0; {playerName}, you have {heart} and {flag} flags.")
    display_game_board()
    if heart != 0 and flag < 5:
        print(f"{playerName}, you win the game. ")
    else:
       print(f"{playerName}, you lose the game. ")
    
# script execution
if __name__ == "__main__":
    main_game()

