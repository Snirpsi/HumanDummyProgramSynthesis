#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words and opens fruits. """    
    
    words = open('fruits.txt').read().splitlines()
    
    for word in words:
        
        word = word.strip()
        
        if word != "":
            
            print(word)
            
        else:
            
            print('')
            
    