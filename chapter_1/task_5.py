import random

def main():
    rand = random.random()
    if rand <= 0.8:
        favourite = "dogs"  # change this
    elif rand <= 0.9:
        favourite = "cats"
    else:
        favourite = "bast"

    print("I love " + favourite)


main()
