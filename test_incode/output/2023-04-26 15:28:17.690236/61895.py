#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers and adds a port. """    
    port = 1
    
    while True:
        number = input('Enter a number: ')
        
        if number == 'done':
            break
        
        number = int(number)
        
        if number < 0 or number > 10:
            print('Invalid number')
            continue
        
        port += 1
        
        print('Port #', port)
        print('Number:', number)
        print('')
        
    print('Done')
    
