#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes user input and prints a list of words. """    
    
    words = []
    
    while(True):
        
        words.append(input("Enter a word: "))
        
        if(len(words) == 0):
            break
        
    print("\n".join(words))
    
    
