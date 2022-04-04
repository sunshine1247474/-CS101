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
            x, y = int(input("x position: ")), int(input("y position: "))
            if board()[x - 1][y - 1] == int:
                print("this place already has a number")
                return check_position()
            if board()[x - 1][y - 1] == "🏳":
                print("unfortunately you fel on a mine :(")
            return position(x, y)
        except ValueError:
            print("not a number")
            return check_position()
        except IndexError:
            print("out of range")
            return check_position()
    return


# this function is generating random numbers withing opening
def position(x, y):
    rand = random.randint(1, 3)
    board()[y - 1][x - 1] = rand
    print(board_table())
    print(str(rand) + " mines near by\nwhich spot are you willing to open next?")
    return check_position()


# this function is used to clean the nine diameter of a number
# def clean_board():

# this is where the computer sets the mines and if we want we can call the function to see them

def flag(none):
    flag_number = int(stage * stage * 0.4)
    for i in range(flag_number - 1):
        randR = random.randint(0, stage - 1)
        randC = random.randint(0, stage - 1)
        if board()[randR][randC] != "🏳":
            board()[randR][randC] = "🏳"
    print(none)
    return board_table()


flag("\nthis is generally were you're mines are")
