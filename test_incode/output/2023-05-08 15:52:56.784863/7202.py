#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that returns user input.
    while True:
        answer = input("Enter a number: ")
        if answer == "":
            print("You did not enter a number")
        else:
            print(answer)

