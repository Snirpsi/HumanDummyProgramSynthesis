#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that opens user input.
    while True:
        answer = input('Enter a number: ')
        try:
            answer = int(answer)
        except ValueError:
            print('That was not a valid number. Please try again.')
        else:
            break
    #A loop that prints the number the user entered.
    while True:
        print(answer)
        answer = input('Enter a number: ')
        try:
            answer = int(answer)
        except ValueError:
            print('That was not a valid number. Please try again.')
        else:
            break

