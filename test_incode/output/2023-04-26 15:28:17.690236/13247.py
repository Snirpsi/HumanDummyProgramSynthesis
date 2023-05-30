#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts all ports or enumerates a list of words. """    
    ports = enumerate('abcdefghijklmnopqrstuvwxyz')
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for port in ports:
        print(port