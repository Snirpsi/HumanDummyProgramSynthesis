#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words or iterates over numbers. """    
    
    import sys
    
    number = int(sys.argv[1])
    
    if number > 0:
        
        word = ""
        
        for i in range(number):
            
            word = word + str(i) + " "
        
        print(word)
        
    elif number < 0:
        
        word = ""
        
        for i in range(-number):
            
            word = word + str(i) + " "
        
        print(word)
        
    else:
        
        print("Usage: python word.py number")
        
