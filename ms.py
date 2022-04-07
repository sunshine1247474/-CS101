import random

# importing random library and using randint func to set board size.
stage = random.randint(3, 5)

"""
Below 1 array that includes multiple arrays which will further more be outspread onto a "table".
although table=[] is not a great argument because its mutable we 
are not going to change it since it is const value of every beginning.

the general plan is constantly updating the board and showing the user only the edited board 
that makes up the game. --> board_table()
"""


# this is the starting board
def board(table=[]):
    for i in range(stage):
        table.append(["_"] * stage)
    return table


print("\nthis is your starting board - minesweeper {}x{}".format(stage, stage))


# expanding board into a table. setting up nicely looking x's and y's
def board_table():
    for i in range(stage):
        print(end="  " * 2 + str(i + 1))
    print()

    for i in range(stage):
        print(i + 1, board()[i])


"""
yay, our first board table actually exist. we can call it now.
we are not using print because inside the print is made.
if we would return anything inside the function 
it would make sense to print the output - print(board_table()) 
"""

board_table()

# this function should expose spots
"""

# this function is generating random numbers withing opening
def expose(x, y):
    check_position(x, y)
    rand = random.randint(1, 3)
    board()[y - 1][x - 1] = rand
    print(board_table())
    print(str(rand) + " mines near by\nwhich spot are you willing to open next?")
    return position(x, y)
"""


# expect to return flags on board for development stage
def flag(none):
    flag_number = int(stage * stage * 0.4)
    for i in range(flag_number - 1):
        randR = random.randint(0, stage - 1)
        randC = random.randint(0, stage - 1)
        if board()[randR][randC] != "🏳":
            board()[randR][randC] = "🏳"
    print(none)
    return board_table()


"""
where the numbers already set, we obviously wouldn't want the numbers
to be visible, so we intend to make it private, challenging...
"""  # virtual private board


def vpb():
    # flag computation algorithm
    x = -1
    y = 0
    for i in board():
        for l in i:
            x += 1
            if l == "🏳":
                print(f'x = {x}, y = {y} found flag')
            if x + 1 == stage:
                x = -1
                y += 1


flag("\nthis is generally were your mines are")
print(vpb())
