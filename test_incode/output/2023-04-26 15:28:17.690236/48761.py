#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input. """    
    while True:
        answer = input('Enter your number: ')
        try:
            number = float(answer)
            break
        except ValueError:
            print('Invalid input')
            continue
    print('The answer is {}'.format(number))
