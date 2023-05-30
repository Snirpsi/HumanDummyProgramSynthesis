#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input or enumerates user input. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            break
        except ValueError:
            print('Invalid input. Try again.')
            continue
    
    total = 0
    for number in range(1, number + 1):
        total += number
    
    print('The total is', total)
    
