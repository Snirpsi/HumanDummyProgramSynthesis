#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that calculates user input.
    while True:
        answer = int(input('Enter a number: '))
        if answer == -1:
            break
        else:
            print(answer)

