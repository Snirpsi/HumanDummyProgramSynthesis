#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that iterates over user input.
    while True:
        answer = input('Enter a number: ')
        try:
            answer = int(answer)
        except ValueError:
            print('That was not a valid number')
        else:
            print(answer)
            break

