#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers or iterates over words. """    
    
    while True:
        words = input("Enter a word: ").split()
        
        for word in words:
            print(word)
        
        print("\nPress Enter to continue.")
        
        input()
        
