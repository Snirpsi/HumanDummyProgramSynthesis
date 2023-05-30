#!/usr/bin/python3
if __name__ == '__main__':
    #A function that calculates user input.
    answer = int(input("Enter a number: "))
    if answer > 10:
        print("Too high")
    elif answer < 10:
        print("Too low")
    else:
        print("Correct")

