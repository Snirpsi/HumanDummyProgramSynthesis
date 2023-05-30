#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that requests user input.
    while True:
        answer = input('Enter a number: ')
        try:
            answer = int(answer)
        except ValueError:
            print('That was not a number!')
        else:
            print('You entered', answer)
            break

