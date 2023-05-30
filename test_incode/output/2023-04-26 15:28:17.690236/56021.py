#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or stores fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s [fruit]' % sys.argv[0])
        sys.exit()
    
    fruit = sys.argv[1]
    
    if fruit == 'fruit':
        print('Enter your favorite fruit:')
        
        while True:
            fruit = input('> ')
            if fruit == 'quit':
                break
            
        print('You chose: %s' % fruit)
        
    elif fruit == 'apple':
        print('Enter your favorite fruit:')
        
        while True:
            fruit = input('> ')
            if fruit == 'quit':
                break
            
        print('You chose: %s' % fruit)
        
    elif fruit == 'banana':
        print('Enter your favorite fruit:')
        
        while True:
            fruit = input('> ')
            if fruit == 'quit':
                break
            
        print('You chose: %s' % fruit)
        
    else:
        print('Invalid input')
        
