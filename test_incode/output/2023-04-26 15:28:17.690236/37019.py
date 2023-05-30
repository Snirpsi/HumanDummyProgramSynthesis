#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words or prints all ports. """    
    while True:
        words = input("Enter words: ")
        words = words.split()
        
        for word in words:
            print(word*