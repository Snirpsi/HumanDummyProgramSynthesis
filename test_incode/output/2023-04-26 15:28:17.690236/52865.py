#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number == 0: break
        numbers.append(number)
        print('Numbers stored:', numbers)
        
