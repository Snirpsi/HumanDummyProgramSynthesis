#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words or adds a list of words. """    
    while True:
        words = input("Enter a word, or 'quit': ")
        if words == 'quit':
            break
        else:
            words = words.split()
            for word in words:
                print(word)
                
