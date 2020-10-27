import random

x_axis = """+-------+"""
two_in = """| o   o |"""
one_in = """|   o   |"""
nan_in = """|       |"""
threet = """| o     |"""
threeb = """|     o |"""

def print_dice(arr: [int]):
    #top
    for i in range(len(arr)):
        print(x_axis, end=' ')
    print()
    #top row
    for i in range(len(arr)):
        if arr[i] in {4,5,6}:
            print(two_in, end=' ')
        elif arr[i] in {2,3}:
            print(threet, end=' ')
        else:
            print(nan_in, end=' ')
    print()
    #middle row
    for i in range(len(arr)):
        if arr[i] in {6}:
            print(two_in, end=' ')
        elif arr[i] in {1, 3, 5}:
            print(one_in, end=' ')
        else:
            print(nan_in, end=' ')
    print()
    #bottom row
    for i in range(len(arr)):
        if arr[i] in {4, 5, 6}:
            print(two_in, end=' ')
        elif arr[i] in {2, 3}:
            print(threeb, end=' ')
        else:
            print(nan_in, end=' ')
    print()
    #bottom
    for i in range(len(arr)):
        print(x_axis, end=' ')
    print()

def parse_keep(roll, keep):
    if keep == 'q':
        quit(-1)
    ret =[]
    for char in keep:
        if char in {'0', '1', '2', '3', '4'}:
            ret.append(roll[int(char)])
    return ret

def main():
    print("Welcome to Yahtzee")
    input("Press any key to roll: ")
    while True:
        x = 0
        kept = []
        while x < 3:
            roll = kept + [random.randint(1, 6) for i in range(5-len(kept))]
            print_dice(roll)
            if x != 2:
                kept = parse_keep(roll, input("Which dice would you like to keep?\n"))
            x += 1
        if input("Press q to quit, or any other key to roll again: ") == 'q':
            quit(0)

if __name__ == '__main__':
    main()
