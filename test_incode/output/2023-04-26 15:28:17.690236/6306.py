#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and returns numbers. """    
    
    words = ['hello', 'world', 'how', 'are', 'you', 'doing', 'today']
    
    numbers = [int(i) for i in words]
    
    print(numbers)
    
