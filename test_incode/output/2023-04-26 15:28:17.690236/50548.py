#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits or enumerates fruits. """    
    while True:
        fruit = input('What fruit do you like? ')
        if fruit == 'quit':
            break
        else:
            print('You chose', fruit)
            
    print('Goodbye!')
    
