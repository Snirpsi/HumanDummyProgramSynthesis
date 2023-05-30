#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words and removes user input. """    
    while True:
        words = input("Enter a word: ").split()
        if len(words) == 0:
            break
        else:
            words = [word.lower() for word in words]
            words = [word for word in words if word not in 