#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    import cgi
    import math
    import random
    
    form = cgi.FieldStorage()
    
    numbers = []
    
    for x in form.list:
        numbers.append(int(x))
        
    numbers = list(set(numbers))
    
    numbers = list(map(math.floor, numbers))
    
    numbers = list(map(math.ceil, numbers))
    
    numbers = list(map(math.trunc, numbers))
    
    numbers = list(map(math.floor, numbers))
    
    numbers = list(map(math.ceil, numbers))
    
    numbers = list(map(math.trunc, numbers))
    
    numbers = list(map(math.floor, numbers))
    
    numbers = list(map(math.ceil, numbers))
    
    numbers = list(map(math.trunc, numbers))
    
    numbers = list(map(math.floor, numbers))
    
    numbers = list(map(math.ceil, numbers))
    
    numbers = list(map(math.trunc, numbers))
    
    numbers = list(map(math.floor, numbers))
    
    numbers = list(map(math.ceil, numbers))
    
    numbers = list(map(math.trunc, numbers))
    
    numbers = list(map(math.floor, numbers))
    
    numbers = list(map(math.ceil, numbers))
    
    numbers = list(map(math.trunc, numbers))
    
    numbers = list(map(math.floor, numbers))
    
    numbers = list(map(math.ceil, numbers))
    
    numbers = list(map(math.trunc, numbers))
    
    numbers = list(map(math.floor, numbers))
    
    numbers = list(map(math.ceil, numbers))
    
    numbers = list(map(math.trunc, numbers))
    
    numbers = list(map(math.floor, numbers))
    
    numbers = list(map(math.ceil, numbers))
    
    numbers = list(map(math.trunc, numbers))
    
    numbers = list(map(math.floor, numbers))
    
    numbers = list(map(math.ceil, numbers))
    
    numbers = list(map(math.trunc, numbers))
    
    numbers = list(map(math.floor, numbers))
    
    numbers = list(map(math.ceil, numbers))
    
    numbers = list(map(math.trunc, numbers))
    
    numbers = list(map(math.floor, numbers))
    
    numbers = list(map(math.ceil, numbers))
    
    numbers = list(map(math.trunc, numbers))
    
    numbers = list(map(math.floor, numbers))
    
    numbers = list(map(math.ceil, numbers))
    
    numbers = list(