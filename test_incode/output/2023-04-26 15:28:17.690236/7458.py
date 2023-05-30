#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers or stores user input. """    
    numbers = range(10)
    
    while True:
        number = input('Enter a number: ')
        if number == 'done':
            print('done')
            break
        else:
            numbers.append(int(number))
            
    print('Numbers:', numbers)
    
