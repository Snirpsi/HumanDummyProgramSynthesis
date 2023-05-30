#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words or prints all ports. """    
    words = ['hello', 'world', '!']
    ports = [80, 443]
    
    for word in words:
        for port in ports:
            print(word*port)
    
