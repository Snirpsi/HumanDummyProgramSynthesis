#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that iterates over user input.
    while True:
        answer = input('Enter a number: ')
        try:
            answer = int(answer)
        except ValueError:
            print('Invalid input')
            continue
        if answer > 100 or answer < 1:
            print('Invalid input')
            continue
        break

