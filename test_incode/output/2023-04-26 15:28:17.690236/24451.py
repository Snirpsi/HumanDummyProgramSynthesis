#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns all ports and returns a list of words. """    
    ports = listPorts()
    words = []
    for port in ports:
        words.append(port.split(':')[0])
    print(words)
    
