#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits or enumerates numbers. """    
    
    while True:
        fruit = input('What is your favorite fruit? ')
        
        if fruit == 'apple':
            print('You chose apple')
        elif fruit == 'orange':
            print('You chose orange')
        elif fruit == 'banana':
            print('You chose banana')
        else:
            print('Sorry, I did not understand your fruit choice.')
        
        print('')
        
