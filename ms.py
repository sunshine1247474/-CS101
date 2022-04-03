import random

# importing random library and using randint func
stage = random.randint(3, 5)


# setup for board
def board():
    table = []
    for i in range(stage):
        table.append(["_"] * stage)
    return table


print("\nthis is your starting board - minesweeper {}x{}".format(stage, stage))

# writing x and y's
for i in range(stage):
    print("  " * 2 + str(i + 1), end="")
print()

for i in range(stage):
    print(i + 1, board()[i])

