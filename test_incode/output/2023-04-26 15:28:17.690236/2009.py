#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words and iterates over a port. """    
    port = "/dev/ttyUSB0"
    words = read_words(port)
    for word in words:
        print(word)
    
