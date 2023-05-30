#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and calculates a port. """    
    words = []
    while True:
        words.append(input("Enter a word: "))
        if len(words) == 3:
            break
    print(calculate_port(words))

<|/ file source=github filename=