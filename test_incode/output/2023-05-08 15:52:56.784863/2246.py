#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that requests user input.
    while True:
        answer = input("Enter a number: ")
        if answer == "quit":
            break
        else:
            print(int(answer))

