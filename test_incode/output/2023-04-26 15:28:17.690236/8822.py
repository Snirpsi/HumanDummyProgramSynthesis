#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers and stores user input. """    
    numbers = []
    while True:
        numbers.append(int(input('Enter a number: ')))
        if numbers[-1] == numbers[-2]:
            break
        else:
            print('Sorry, you entered a 