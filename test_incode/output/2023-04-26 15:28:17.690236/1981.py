#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits or prints fruits. """    
    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'quit':
            print('Goodbye!')
            break
        else:
            print('You chose: ' + fruit)
            
    print('Goodbye!')
    
