#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words and prints all ports. """    
    
    words = []
    
    for word in open('words.txt'):
        words.append(word.rstrip())
    
    ports = []
    
    for word in words:
        ports.append(word)
    
    for port in ports:
        print('{}: {}'.format(port, len(port