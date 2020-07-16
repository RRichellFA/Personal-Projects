from random import randint


def dice(sides):
    """
    :param sides: How many side the dice have.
    :return: Random number, min = 1, max = sides.
    """
    return randint(1, sides)


while True:
    rolls = int(input("Roll how many times? "))
    sides = int(input(f"Roll {rolls} dices of how many sides? "))
    for c in range(rolls):
        print(dice(sides))
