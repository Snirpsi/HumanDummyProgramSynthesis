#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes fruits. """    
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    for fruit in fruits:
        
        if fruit not in fruits:
            
            print('The fruit ' + fruit + ' is not in the list')
            
        else:
            
            print('The fruit ' + fruit + ' is in the list')
            
