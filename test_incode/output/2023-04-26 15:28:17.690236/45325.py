#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and multiplyes user input. """    
    
    words = ['hello', 'world', 'python']
    
    multiplier = 1
    
    for word in words:
        multiplier = multiplier * int(word)
        
    print(multiplier)
    
