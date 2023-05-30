#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port and multiplyes a list of words. """    
    
    port = "/dev/ttyUSB0"
    words = ["hello", "world"]
    
    for word in words:
        print(word*