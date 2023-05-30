#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input. """    
    while True:
        try:
            answer = int(input('Enter your answer: '))
            break
        except ValueError:
            print('Invalid input. Try again.')
            continue
