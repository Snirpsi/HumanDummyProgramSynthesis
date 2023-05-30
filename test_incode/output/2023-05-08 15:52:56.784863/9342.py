#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that iterates over user input.
    while True:
        answer = input('Enter a number: ')
        try:
            answer = int(answer)
        except ValueError:
            print('That is not a number!')
        else:
            break
    print('You entered a number!')

