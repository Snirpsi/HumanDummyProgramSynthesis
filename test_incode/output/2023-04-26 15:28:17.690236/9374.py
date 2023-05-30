#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words and opens user input. """    
    
    words = []
    
    while(True):
        words.append(input("Enter a word: "))
        
        if words[-1] == 'q':
            break
    
    print(words)
    
