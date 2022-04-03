import random

stage = random.randint(3, 5)


def board():
    table = []
    for i in range(stage):
        table.append(["_"] * stage)
    return table


print("\nthis is your starting board - minesweeper {}x{}".format(stage, stage))

for i in range(stage):
    print("  "*2 + str(i+1), end="")
print()

for i in range(stage):
    print(i + 1, board()[i])

