#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates fruits or iterates over a list of words. """    
    
    words = ['apple', 'banana', 'orange', 'pear']
    
    fruit = words[0]
    
    for word in words:
        if word == fruit:
            print('Found fruit!')
            break
        else:
            print('Not found!')
            
    print('Done!')
    
