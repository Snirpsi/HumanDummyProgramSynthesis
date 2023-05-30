#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that opens user input.
    while True:
        line = input('Enter a number: ')
        try:
            number = int(line)
        except ValueError:
            print('That is not a valid number.')
        else:
            break
    print('The number you entered is', number)

