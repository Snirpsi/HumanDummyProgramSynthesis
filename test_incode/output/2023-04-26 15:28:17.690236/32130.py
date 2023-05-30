#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words and removes numbers. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for word in words:
        print(word)
        
        number = word[-1]
        
        if number.isdigit():
            word