#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words and removes user input. """    
    while True:
        words = input("Enter a word: ").split()
        words = [word.lower() for word in words]
        
        if words:
            words = [word for word in words if word not in words]
            print(" ".join(words))
        else:
            break
        
