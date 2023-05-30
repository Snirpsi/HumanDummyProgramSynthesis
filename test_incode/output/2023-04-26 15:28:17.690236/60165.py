#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words. """    
    while True:
        words = []
        words = input("Enter a word: ").split()
        if words:
            print(" ".join(words))
        else:
            print("No words entered")
            
