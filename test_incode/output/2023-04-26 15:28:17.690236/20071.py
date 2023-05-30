#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports and returns a list of words. """    
    
    ports = [int(i) for i in input().split()]
    
    words = []
    
    for port in ports:
        words.append(str(port*