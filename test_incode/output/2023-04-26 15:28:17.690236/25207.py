#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports and converts a list of words. """    
    ports = [int(i) for i in input().split()]
    words = [int(i) for i in input().split()]
    
    words = [word*port for word, port in zip(words, ports)]
    
    print(" ".join(str(word) for word in words))
    
