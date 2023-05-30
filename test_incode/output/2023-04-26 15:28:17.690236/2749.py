#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words or converts a list of numbers. """    
    while True:
        line = input()
        if line == 'exit':
            break
        else:
            words = line.split()
            print(" ".join(map(str, words)))
