#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits or returns a port. """    
    
    fruit = enumerate_fruits()
    
    if fruit == 'apple':
        print('The fruit is apple')
    elif fruit == 'orange':
        print('The fruit is orange')
    elif fruit == 'banana':
        print('The fruit is banana')
    else:
        print('The fruit is neither apple nor orange')
    
