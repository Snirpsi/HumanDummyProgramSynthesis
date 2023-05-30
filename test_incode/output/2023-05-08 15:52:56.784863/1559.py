#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that calculates user input.
    while True:
        answer = int(input('Enter a number: '))
        if answer == 5:
            break
        else:
            print('Sorry, that number is not valid.')

