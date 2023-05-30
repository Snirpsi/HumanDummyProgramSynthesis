#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers or calculates words. """    
    
    words = removeNumbers(sys.argv[1])
    
    for word in words:
        print(word)
        
