#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers or stores words. """    
    
    words = []
    
    while True:
        number = int(input('Enter a number: '))
        
        if number < 0:
            print('Invalid number')
            continue
        
        if number == 0:
            break
        
        words.append(number)
        
        print('The number you entered is', number)
        print('The words contained are', words)
        
    print('The words contained are', words)
    
