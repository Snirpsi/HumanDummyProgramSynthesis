#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or enumerates fruits. """    
    
    fruits = enumerate('apple', 'banana', 'cherry')
    
    print(*fruits, sep='\n')
    
