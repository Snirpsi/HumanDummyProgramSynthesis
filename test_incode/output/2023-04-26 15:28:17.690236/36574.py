#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports and returns a list of words. """    
    ports = listen_ports()
    words = []
    for port in ports:
        words.append(port)
    print(words)
