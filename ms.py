import random

# importing random library and using randint func
stage = random.randint(3, 5)


# setup for board that will later on be used
def board(table=[]):
    for i in range(stage):
        table.append(["_"] * stage)
    return table


print("\nthis is your starting board - minesweeper {}x{}".format(stage, stage))


# basically the beginning of x and y of our table (prints 1 to random number at x's and y's)
def board_table():
    for i in range(stage):
        print(end="  " * 2 + str(i + 1))
    print()

    for i in range(stage):
        print(i + 1, board()[i])


# yay, our first board table actually exist
board_table()


# this function should return fair game and status
def check_position(x=0, y=0):
    while x <= stage and y <= stage:
        try:
            x, y = int(input("y position: ")), int(input("x position: "))
            return position(x, y)
        except ValueError:
            print("your input got to be in the range")

    return check_position()


# this function is generating random numbers withing opening
def position(x, y):
    rand = random.randint(1, 4)
    board()[y - 1][x - 1] = rand
    print(board_table())
    print(str(rand) + " mines near by\nwhich spot are you willing to open next?")
    return check_position()


# this function is used to clean the nine diameter of a number
# def clean_board():

# this is where the computer sets the mines and if we want we can call the function to see them
def flag():
    flag_number = int(stage / 25)
    rand = random.randint(0, stage)
    for i in range(1, flag_number):
        board()[rand][rand] = "🏳"


check_position()
