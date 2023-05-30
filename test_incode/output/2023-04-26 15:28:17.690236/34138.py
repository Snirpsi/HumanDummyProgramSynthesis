#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words or prints words. """    
    
    words = input("Enter a word: ")
    
    if len(words) == 0:
        print("No words entered")
    else:
        print(words)
        
